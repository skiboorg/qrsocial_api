from rest_framework import serializers
from .models import *


class BlogItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogItem
        fields = '__all__'



