from rest_framework import serializers
from .models import *
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = [
            'id',
            'avatar',
            'fio',
            'nickname',
            'suid',
            'streamer_rating'
        ]
    def get_avatar(self, obj):
        if obj.avatar:
            return self.context['request'].build_absolute_uri(obj.avatar.url)
        else:
            return '/no-avatar.svg'

class StreamLikeSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    class Meta:
        model = StreamLike
        fields = ['users']


class StreamSerializer(serializers.ModelSerializer):
    streamer = UserSerializer(many=False,required=False,read_only=True)
    url = serializers.CharField(source='get_stream_url',required=False,read_only=True)
    chat_id = serializers.CharField(source='get_stream_chat_id',required=False,read_only=True)
    likes = StreamLikeSerializer(many=True)
    class Meta:
        model = Stream
        fields = '__all__'


