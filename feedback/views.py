from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from .serializers import *


class AddFeedback(generics.CreateAPIView):
    serializer_class = FeedBackFormSerializer
    queryset = FeedBackForm.objects.all()

