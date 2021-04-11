from django.urls import path,include
from . import views

urlpatterns = [


    path('get_streams_by_user_nickname', views.GetStreamsByUserNickmane.as_view()),
    path('get_stream_by_uid', views.GetStreamByUID.as_view()),
    path('get_streams_for_home_page', views.GetStreamsForHomePage.as_view()),
    path('add_stream', views.AddStream.as_view()),
    path('update_stream', views.UpdateStream.as_view()),
    path('add_remove_like', views.AddRemoveLike.as_view()),





]
