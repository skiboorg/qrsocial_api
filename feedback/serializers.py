from rest_framework import serializers
from .models import *

class FeedBackFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBackForm
        fields = '__all__'

