
from rest_framework import serializers
from .models import *
from user.models import  User

class UserSerializerForGift(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'avatar',
            'fio',
            'nickname',
            'is_online'
        ]

class GiftSerializer(serializers.ModelSerializer):
    print('GiftSerializer')
    class Meta:
        model = Gift
        fields = '__all__'


class UserGiftSerializer(serializers.ModelSerializer):
    from_user = UserSerializerForGift(many=False)
    user = UserSerializerForGift(many=False)
    gift = GiftSerializer(many=False)
    class Meta:
        model = UserGift
        fields = '__all__'

class DonaterSerializer(serializers.ModelSerializer):
    from_user = UserSerializerForGift(many=False)
    class Meta:
        model = Donater
        fields = '__all__'
