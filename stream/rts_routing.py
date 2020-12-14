from django.urls import path
from stream.consumers import *

websocket_urlpatterns = [
    path('ws/video_call/signal/<room_name>', VideoCallSignalConsumer),
]
