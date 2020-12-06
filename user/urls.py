from django.urls import path,include
from . import views

urlpatterns = [


    path('me/', views.GetUser.as_view()),
    path('update/', views.UserUpdate.as_view()),
    path('get_user_info_by_nickname/', views.GetUserInfoByNickname.as_view()),
    path('get_streamers/', views.GetStreamers.as_view()),
    path('get_user_tags', views.GetUserTags.as_view()),
    path('add_to_balance', views.AddToBalance.as_view()),

]
