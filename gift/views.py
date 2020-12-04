from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *
from user.models import User
from history.services import create_user_history


class GetUserSendedGifts(generics.ListAPIView):
    serializer_class = UserGiftSerializer

    def get_queryset(self):
        return UserGift.objects.filter(from_user__nickname=self.request.query_params['nickname'])


class GetUserGifts(generics.ListAPIView):
    serializer_class = UserGiftSerializer

    def get_queryset(self):
        return UserGift.objects.filter(user__nickname=self.request.query_params['nickname'])


class GetAllGifts(generics.ListAPIView):
    serializer_class = GiftSerializer
    queryset = Gift.objects.all()


class SendGiftToUser(APIView):
    def post(self, request):
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
        create_user_history(gift_to_user, f'Подарок . Пополнен баланс на {gift.price}.')
        create_user_history(gift_from_user, f'Подарок . С баланса спасано {gift.price}.')
        return Response(status=200)
