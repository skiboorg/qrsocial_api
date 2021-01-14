from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from .models import *
from user.models import User

class AddOrDeleteFriendByNickname(APIView):
    def post(self,request):
        data = request.data
        # print(data)
        friend = User.objects.get(nickname=data['nickname'])
        all_friends = FriendList.objects.get(user=request.user)
        friend_all_friends = FriendList.objects.get(user=friend)
        if data['action'] == 'delete':
            all_friends.friend_list.remove(friend)
            friend_all_friends.friend_list.remove(request.user)
        else:
            all_friends.friend_list.add(friend)
            friend_all_friends.friend_list.add(request.user)
        return Response(status=200)

class GetFriendsById():
    pass
