from django.urls import path,include
from . import views

urlpatterns = [
    path('get_galleries_by_user_nickname', views.GetGalleriesByUserNickname.as_view()),
    path('add_gallery', views.AddGallery.as_view()),
    path('delete_gallery', views.DeleteGallery.as_view()),






]
