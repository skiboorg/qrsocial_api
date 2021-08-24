from django.urls import path,include
from . import views

urlpatterns = [


    path('get_chat_messages', views.MessagesList.as_view()),
    path('get_stikers', views.GetStikers.as_view()),
    path('get_chat', views.GetChat.as_view()),
    path('get_chat_by_users', views.GetChatByUsers.as_view()),
    path('get_chat_by_users_for_girl', views.GetChatByUsers4Girl.as_view()),
    path('set_chat_read/<int:chat_id>', views.SetChatRead.as_view()),
    path('all', views.ChatsList.as_view()),
    path('add/<int:chat_id>', views.ChatAdd.as_view()),
    path('new_message', views.ChatNewMessage.as_view()),

]
