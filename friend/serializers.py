from rest_framework import serializers
from .models import *
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        exclude = (
            'password',
            'bg_image',
            'balance',
            'vip_update',
            'vip_expire',
            'is_streamer',
            'is_verified',
            'is_email_verified',
            'verify_code',
            'stream_key',
            'channel',
            'groups',
            'user_permissions',
            'is_superuser',
            'is_staff',
            'wechatid',
            'email',
        )

    def get_avatar(self, obj):
        if obj.avatar:
            return self.context['request'].build_absolute_uri(obj.avatar.url)
        else:
            return '/no-avatar.svg'




class FriendListSerializer(serializers.ModelSerializer):
    friend_list = UserSerializer(many=True)
    class Meta:
        model = FriendList
        fields = '__all__'


class FriendApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendApply
        fields = '__all__'

