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
            'nickname'
        ]
    def get_avatar(self, obj):
        if obj.avatar:
            return self.context['request'].build_absolute_uri(obj.avatar.url)
        else:
            return '/no-avatar.svg'



class PostLikeSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    class Meta:
        model = PostLike
        fields = ['users']


class PostCommentSerializer(serializers.ModelSerializer):
    # friend_list = UserSerializer(many=True)
    owner = UserSerializer(many=False)
    created = serializers.CharField(source='get_humanize_time')
    class Meta:
        model = PostComment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False)
    comments = PostCommentSerializer(many=True)
    comments_show = serializers.BooleanField(default=False)
    comments_count = serializers.IntegerField(source='get_comments_count')
    created = serializers.CharField(source='get_humanize_time')
    likes = PostLikeSerializer(many=True)



    class Meta:
        model = Post
        fields = '__all__'



