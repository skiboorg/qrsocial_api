import json
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from rest_framework import generics
from django.http import Http404
from history.services import create_user_history

class GetUserByID(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.filter()

class GetUser(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user
    # def get(self, request):
    #     user = request.user
    #     serializer = UserSerializer(user, many=False)
    #     return Response(serializer.data)

class UserUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        print(json.loads(request.data['userData']))
        print(request.FILES)
        data = json.loads(request.data['userData'])
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            for f in request.FILES.getlist('avatar'):
                print(f'f=')
                user.avatar = f
                user.save(update_fields=['avatar'])
            for f1 in request.FILES.getlist('bg_image'):
                print(f1)
                user.bg_image = f1
                user.save()
            if data['password1'] and data['password1'] == data['password2']:
                user.set_password(data['password1'])
                user.save()
            return Response(status=200)

        else:
            print(serializer.errors)
            return Response(status=400)


class GetUserInfoByNickname(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        nickname = self.request.query_params.get('nickname')
        try:
            user = User.objects.get(nickname=nickname)
        except:
            raise Http404

        return user


class GetUserTags(generics.ListAPIView):
    serializer_class = UserTagSerializar
    queryset = UserTag.objects.all()


class GetStreamers(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.query_params.get('at_home') == 'true':
            return User.objects.filter(is_streamer=True, is_show_at_home=True)
        else:
            return User.objects.filter(is_streamer=True)

class AddToBalance(APIView):
    def post(self,request):
        print(request.data)
        user = request.user
        user.balance += request.data['amount']
        user.save()
        create_user_history(user, f'Пополнение счета {request.data["amount"]}. ')
        return Response(status=200)
