from rest_framework import serializers
from .models import *
from user.models import User


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id','image']


class GallerySerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    class Meta:
        model = Gallery
        fields = '__all__'



