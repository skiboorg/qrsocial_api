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
            'is_online'
        ]

    def get_avatar(self, obj):
        if obj.avatar:
            return self.context['request'].build_absolute_uri(obj.avatar.url)
        else:
            return '/no-avatar.svg'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id','image']


class GallerySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Gallery
        fields = '__all__'

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, required=False, read_only=True)
    class Meta:
        model = Video
        fields = '__all__'

class GalleryFullSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False, required=False, read_only=True)
    images = ImageSerializer(many=True)
    class Meta:
        model = Gallery
        fields = '__all__'