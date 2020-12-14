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


class GetUserTop3Donaters(generics.ListAPIView):
    serializer_class = DonaterSerializer

    def get_queryset(self):
        return Donater.objects.filter(to_user__nickname=self.request.query_params['nickname']).order_by('-summ')[:3]


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
