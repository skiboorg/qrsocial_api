from django.urls import path,include
from . import views

urlpatterns = [
    path('get_galleries_by_user_nickname', views.GetGalleriesByUserNickname.as_view()),
    path('get_videos_by_user_nickname', views.GetVideosByUserNickname.as_view()),
    path('get_banners', views.GetBanners.as_view()),
    path('add_gallery', views.AddGallery.as_view()),
    path('update_gallery', views.UpdateGallery.as_view()),
    path('delete_image_by_id/<int:pk>', views.DeleteImageById.as_view()),
    path('add_img_in_gallery_by_id', views.AddImageInGalleryById.as_view()),
    path('add_video', views.AddVideo.as_view()),
    path('get_videos', views.GetVideos.as_view()),
    path('get_last_gallery', views.GetLastGallery.as_view()),
    path('get_last_user_images', views.GetLastUserImages.as_view()),





]
