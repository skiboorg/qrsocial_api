from django.urls import path,include
from . import views

urlpatterns = [


    path('get_posts_by_user_nickname', views.GetPostsByUserNickmane.as_view()),
    path('add_comment', views.AddComment.as_view()),
    path('add_post', views.AddPost.as_view()),
    path('delete_post', views.DeletePost.as_view()),
    path('add_remove_like_to_post', views.AddRemoveLikeToPost.as_view()),




]
