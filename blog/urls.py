from django.urls import path,include
from . import views

urlpatterns = [


    path('get_items', views.GetItems.as_view()),
    path('get_item', views.GetItem.as_view()),






]
