from django.urls import path,include
from . import views

urlpatterns = [
    path('add_feedback', views.AddFeedback.as_view()),

]
