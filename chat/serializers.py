from rest_framework import exceptions, serializers
from djoser.conf import settings
from .models import *
from user.models import User

class UserSerializerForMessage(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'avatar',
            'fio',
            'nickname',
            'is_online',
            'is_vip'
        ]
class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'avatar',
            'fio',
            'nickname',
            'is_online',
            'is_vip'
        ]
    def get_avatar(self, obj):
        if obj.avatar:
            return self.context['request'].build_absolute_uri(obj.avatar.url)
        else:
            return '/no-avatar.svg'


class ChatSerializer(serializers.ModelSerializer):
    starter = UserSerializer()
    opponent = UserSerializer()
    class Meta:
        model = Chat
        fields = [
            'id',
            'isNewMessages',
            'updatedAt',
            'starter',
            'opponent',
            'is_stream_chat'

            ]

class ChatsSerializer(serializers.ModelSerializer):
    starter = UserSerializer()
    opponent = UserSerializer()
    # last_message = serializers.CharField(source='get_last_message_text')
    # last_message_user_id = serializers.CharField(source='get_last_message_user_id')
    # last_message_user_name = serializers.CharField(source='get_last_message_user_name')
    # last_message_user_status = serializers.BooleanField(source='get_last_message_user_status')
    # last_message_user_avatar = serializers.CharField(source='get_last_message_user_avatar')
    chat_opened = serializers.BooleanField(default=False)
    class Meta:
        model = Chat
        fields = [
            'id',
            'isNewMessages',
            # 'updatedAt',
            'starter',
            'opponent',
            'chat_opened',
            'is_stream_chat'
            # 'last_message',
            # 'last_message_user_id',
            # 'last_message_user_avatar',
            # 'last_message_user_name',
            # 'last_message_user_status'

                  ]
class StikerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stiker
        fields = '__all__'



class StikerGroupSerializer(serializers.ModelSerializer):
    stikers = StikerSerializer(many=True)
    class Meta:
        model = StikerGroup
        fields = '__all__'




class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializerForMessage(many=False)
    stiker = StikerSerializer(many=False)
    class Meta:
        model = Message
        fields = [
            'id',
            'chat',
            'user',
            'message',
            'message_translate',
            'image',
            'stiker',
            'createdAt',
                  ]

class MessagesSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    stiker = StikerSerializer(many=False)
    class Meta:
        model = Message
        fields = [
            'id',
            'user',
            'message',
            'message_translate',
            'isUnread',
            'image',
            'stiker',
            'createdAt',
            'chat'
                  ]


