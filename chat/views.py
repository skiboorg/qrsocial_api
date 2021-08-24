import json
from functools import reduce
import requests

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *
from notification.services import createNotification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from notification.models import Notification

channel_layer = get_channel_layer()

class GetChatByUsers(generics.RetrieveAPIView):
    serializer_class = ChatSerializer
    def get_object(self):
        opponent_nickname = self.request.query_params.get('opponent')

        opponent = User.objects.get(nickname=opponent_nickname)
        chat,created = Chat.objects.get_or_create(starter=self.request.user,opponent=opponent)
        if created:
            chat.users.add(self.request.user)
            chat.users.add(opponent)
            print('chat created')
        return chat


class GetChatByUsers4Girl(generics.RetrieveAPIView):
    serializer_class = ChatSerializer

    def get_object(self):
        starter_nickname = self.request.query_params.get('starter')
        starter = User.objects.get(nickname=starter_nickname)
        chat = Chat.objects.get(opponent=self.request.user,starter=starter)
        return chat

class GetChat(generics.RetrieveAPIView):
    serializer_class = ChatSerializer
    def get_object(self):
        chat_id = self.request.query_params.get('chat_id')
        chat = Chat.objects.get(id=chat_id)
        return chat



class MessagesList(generics.ListAPIView):
    """Вывод сообщений в чате"""
    serializer_class = MessagesSerializer
    def get_queryset(self):
        chat_id=self.request.query_params.get('chat_id')
        chat = Chat.objects.get(id=chat_id)
        messages = Message.objects.filter(chat=chat)

        # unread_notifications = Notification.objects.filter(type='chat',user=self.request.user,chat_id=chat_id)
        # unread_notifications.update(is_new=False)

        return messages

    # def get(self,request, chat_id):
    #     chat = Chat.objects.get(id=chat_id)
    #     messages = Message.objects.filter(chat=chat)
    #     serializer = MessagesSerializer(messages, many=True)
    #     return Response(serializer.data)

class ChatsList(generics.ListAPIView):
    """Вывод чатов"""
    serializer_class = ChatsSerializer
    def get_queryset(self):
        chats = Chat.objects.filter(users__in=[self.request.user.id], is_stream_chat=False).order_by('-updatedAt')
        return chats

class SetChatRead(APIView):
    def post(self,request, chat_id):
        chat = Chat.objects.get(id=chat_id)
        messages = chat.messages
        chat.isNewMessages = False
        chat.save()
        messages.update(isUnread=False)
        notify = Notification.objects.filter(user=request.user, chat_id=chat_id)
        notify.delete()
        return Response(status=200)

def check_translate_key():
    import datetime as dt
    from datetime import datetime
    from django.utils import timezone

    key = None
    try:
        key = TraslateKey.objects.get(id=1)
    except:
        data = '{"yandexPassportOauthToken":"AgAAAABQDeFrAATuwSGnF2oKw0vmjJeaO4iggoE"}'
        response = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens', data=data)
        key = response.json().get('iamToken')
        TraslateKey.objects.create(key=key)
        return (key)
    if timezone.now() - key.updated_at > dt.timedelta(hours=6):
        data = '{"yandexPassportOauthToken":"AgAAAABQDeFrAATuwSGnF2oKw0vmjJeaO4iggoE"}'
        response = requests.post('https://iam.api.cloud.yandex.net/iam/v1/tokens', data=data)
        key.key = response.json().get('iamToken')
        key.save()
        return response.json().get('iamToken')
    else:
        return key.key




class ChatAdd(APIView):

    """Добавить сообщение в чат"""
    def post(self,request, chat_id):
        print(request.data)
        im_token = check_translate_key()
        message_lang = request.data['message_lang']
        message_text = json.loads(request.data['message'])
        stiker= json.loads(request.data['stiker'])
        print(message_lang)



        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {im_token}",
        }

        data = {
            "folder_id": "b1grf2b1imq40far6803",
            "texts": [f"{message_text}",],
            "targetLanguageCode": f"{'ru' if message_lang == 'zh' else 'zh'}"
        }
        response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate', headers=headers,
                                 data=json.dumps(data))
        message_translate = response.json().get('translations')[0]['text']

        chat = Chat.objects.get(id=chat_id)
        new_message = Message.objects.create(chat=chat,
                                             user=request.user,
                                             stiker_id=stiker,
                                             message=message_text,
                                             message_translate=message_translate)

        for f in request.FILES.getlist('image'):
            new_message.image = f
            new_message.save(update_fields=['image'])

        message = MessageSerializer(new_message,many=False)
        async_to_sync(channel_layer.group_send)('chat_%s' % chat.id,
                                                {"type": "chat.message", 'message': message.data, 'chatId': chat_id})
        for user in chat.users.all():
            if user != request.user:
                if user.channel:
                    createNotification('chat', user, 'Новое сообщение в чате', '/lk/chats', chat_id=chat.id)
                    async_to_sync(channel_layer.send)(user.channel,
                                                      {
                                                          "type": "user.notify",
                                                          'message': 'Новое сообщенеи в чатеr',
                                                          'event' : 'new_chat_mgs',
                                                          'chatId': chat_id
                                                      })
        return Response(status=201)


class ChatNewMessage(APIView):
    """Добавить сообщение в чат"""
    def post(self,request):
        data = request.data
        chat_opponent = User.objects.get(nickname=data['nickname'])
        c = [request.user.id, chat_opponent.id]
        chats = Chat.objects.annotate(cnt=models.Count('users')).filter(cnt=len(c),is_stream_chat=False) #ADDED  ,is_stream_chat=False
        chat_qs = reduce(lambda qs, pk: qs.filter(users=pk), c, chats)

        if len(chat_qs) == 0:
            chat = Chat.objects.create(starter=request.user, opponent=chat_opponent)
            chat.users.add(request.user)
            chat.users.add(chat_opponent)
        else:
            chat = chat_qs[0]

        # print(request.data)

        # print(msg_to)
        createNotification('chat', chat_opponent, 'Новое сообщение в чате', '/lk/chats',chat_id=chat.id)
        # async_to_sync(channel_layer.send)(chat_opponent.channel, {"type": "user.notify"})

        Message.objects.create(chat=chat,
                               user=request.user,
                               message=data['message'])

        return Response(status=200)

class GetStikers(generics.ListAPIView):
    serializer_class = StikerGroupSerializer
    queryset = StikerGroup.objects.all()