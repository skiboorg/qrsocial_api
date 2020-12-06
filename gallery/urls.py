from django.urls import path,include
from . import views

urlpatterns = [
    path('get_galleries_by_user_nickname', views.GetGalleriesByUserNickname.as_view()),





]
