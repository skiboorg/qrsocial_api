
from rest_framework import serializers
from .models import *
from user.models import User

class UserSerializerForGift(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'avatar',
            'fio',
            'nickname',
            'is_online'
        ]

    def get_avatar(self, obj):
        if obj.avatar:
            return self.context['request'].build_absolute_uri(obj.avatar.url)
        else:
            return '/no-avatar.svg'



class GiftSerializer(serializers.ModelSerializer):
    # print('GiftSerializer')

    class Meta:
        model = Gift
        fields = '__all__'


class UserGiftSerializer(serializers.ModelSerializer):
    from_user = UserSerializerForGift(many=False)
    user = UserSerializerForGift(many=False)
    gift = GiftSerializer(many=False)
    filename = serializers.SerializerMethodField()
    class Meta:
        model = UserGift
        fields = '__all__'
    def get_filename(self, obj):
        if obj.answer_file:
            return obj.answer_file.url.split('/')[::-1][0]

class DonaterSerializer(serializers.ModelSerializer):
    from_user = UserSerializerForGift(many=False)
    class Meta:
        model = Donater
        fields = '__all__'

class StreamDonaterSerializer(serializers.ModelSerializer):
    from_user = UserSerializerForGift(many=False)

    class Meta:
        model = StreamDonater
        fields = [
            'stream',
            'to_user',
            'from_user',
            'summ',

        ]


class GiftCategorySerializer(serializers.ModelSerializer):
    gifts = GiftSerializer(many=True, required=False, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'