from django.urls import path,include
from . import views

urlpatterns = [


    path('get_all', views.GetAllGifts.as_view()),
    path('get_user_gifts', views.GetUserGifts.as_view()),
    path('get_user_sended_gifts', views.GetUserSendedGifts.as_view()),
    path('send_gift_to_user', views.SendGiftToUser.as_view()),





]
