import json
from functools import reduce


from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *
# from notification.services import createNotification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# from notification.models import Notification

channel_layer = get_channel_layer()

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
        return Response(status=200)


class ChatAdd(APIView):
    """Добавить сообщение в чат"""
    def post(self,request, chat_id):
        print(request.data)
        message_text = json.loads(request.data['message'])
        print(message_text)

        chat = Chat.objects.get(id=chat_id)
        new_message = Message.objects.create(chat=chat,
                               user=request.user,
                               message=message_text)

        for f in request.FILES.getlist('image'):
            new_message.image = f
            new_message.save(update_fields=['image'])

        message = MessageSerializer(new_message,many=False)
        async_to_sync(channel_layer.group_send)('chat_%s' % chat.id,
                                                 {"type": "chat.message", 'message': message.data})
        for user in chat.users.all():
            if user != request.user:
                if user.channel:
                    async_to_sync(channel_layer.send)(user.channel,
                                                      {
                                                          "type": "user.notify",
                                                          'message': 'Новое сообщенеи в чатеr',
                                                          'event' : 'new_chat_mgs'
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
        # msg_to = User.objects.get(id=opponent_id)
        # print(msg_to)
        # createNotification('chat', msg_to, 'Новое сообщение в чате', '/lk/chats',chat_id=chat.id)
        # async_to_sync(channel_layer.send)(msg_to.channel, {"type": "user.notify"})

        Message.objects.create(chat=chat,
                               user=request.user,
                               message=data['message'])

        return Response(status=200)

