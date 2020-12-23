from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *
from user.models import User
from history.services import create_user_history
from stream.models import Stream
from chat.models import Chat
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

class GetUserSendedGifts(generics.ListAPIView):
    serializer_class = UserGiftSerializer

    def get_queryset(self):
        return UserGift.objects.filter(from_user__nickname=self.request.query_params['nickname'])

class GetUserTop3Donaters(generics.ListAPIView):
    serializer_class = DonaterSerializer

    def get_queryset(self):
        return Donater.objects.filter(to_user__nickname=self.request.query_params['nickname']).order_by('-summ')[:3]



class GetUserTop3StreamDonaters(generics.ListAPIView):
    serializer_class = StreamDonaterSerializer

    def get_queryset(self):
        try:
            donaters = StreamDonater.objects.filter(stream_id=self.request.query_params.get('stream_id')).order_by('-summ')[:3]
            return donaters
        except:
            return None


class GetUserGifts(generics.ListAPIView):
    serializer_class = UserGiftSerializer

    def get_queryset(self):
        return UserGift.objects.filter(user__nickname=self.request.query_params['nickname'], gift__is_special_gift=False)

class GetUserGiftsSpecial(generics.ListAPIView):
    serializer_class = UserGiftSerializer

    def get_queryset(self):
        return UserGift.objects.filter(user__nickname=self.request.query_params['nickname'], gift__is_special_gift=True)

class GetAllGifts(generics.ListAPIView):
    print('GetAllGifts')
    serializer_class = GiftSerializer
    queryset = Gift.objects.all()


class SendGiftToUser(APIView):
    def post(self, request):
        print(request.data)
        gift = Gift.objects.get(id=request.data['gift_id'])
        gift_from_user = request.user
        gift_to_user = User.objects.get(nickname=request.data['nickname'])
        gift_from_user.balance -= gift.price
        gift_to_user.balance += gift.price
        UserGift.objects.create(from_user=gift_from_user,
                                user=gift_to_user,
                                gift=gift,
                                message=request.data['message'])
        gift_to_user.save()
        gift_from_user.save()
        if request.data['stream']:
            print('This is stream gift')
            stream = Stream.objects.get(id=request.data['stream'])
            stream_chat = Chat.objects.get(stream=stream)
            try:
                donater = StreamDonater.objects.get(to_user=gift_to_user,
                                                    from_user=gift_from_user,
                                                    stream=stream)
                donater.summ += gift.price
                donater.save()
            except StreamDonater.DoesNotExist:
                StreamDonater.objects.create(summ=gift.price,
                                       stream=stream,
                                       to_user=gift_to_user,
                                       from_user=gift_from_user)
            print('sending WS gift message')
            async_to_sync(channel_layer.group_send)('chat_%s' % stream_chat.id,
                                                    {"type": "chat.gift",
                                                     'gift_img': gift.image.url,
                                                     'gift_price': gift.price,
                                                     'gift_message': request.data['message'],
                                                     'gift_from': gift_from_user.nickname,
                                                     'gift_to': gift_to_user.id,

                                                     }
                                                    )

        try:
            donater = Donater.objects.get(to_user=gift_to_user,
                                          from_user=gift_from_user)
            donater.summ += gift.price
            donater.save()
        except Donater.DoesNotExist:
            Donater.objects.create(summ=gift.price,
                                   to_user=gift_to_user,
                                   from_user=gift_from_user)

        create_user_history(gift_to_user, f'Подарок . Пополнен баланс на {gift.price}.')
        create_user_history(gift_from_user, f'Подарок . С баланса спасано {gift.price}.')
        return Response(status=200)
