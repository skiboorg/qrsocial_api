from django.urls import path,include
from . import views

urlpatterns = [


    path('get_all', views.GetAllGifts.as_view()),
    path('get_user_gifts', views.GetUserGifts.as_view()),
    path('get_user_gifts_special', views.GetUserGiftsSpecial.as_view()),
    path('get_user_top3_donaters', views.GetUserTop3Donaters.as_view()),
    path('get_user_top10_donaters', views.GetUserTop10Donaters.as_view()),
    path('get_user_top3_stream_donaters', views.GetUserTop3StreamDonaters.as_view()),
    path('get_user_sended_gifts', views.GetUserSendedGifts.as_view()),
    path('send_gift_to_user', views.SendGiftToUser.as_view()),
    path('gift_answer', views.GiftAnswer.as_view()),





]
