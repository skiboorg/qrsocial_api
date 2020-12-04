from django.urls import path,include
from . import views

urlpatterns = [


    # path('get_friends_by_id/<int:id>', views.GetFriendsById.as_view()),
    path('add_or_delete_friend_by_nickname', views.AddOrDeleteFriendByNickname.as_view()),


]
