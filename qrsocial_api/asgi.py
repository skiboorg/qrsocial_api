import os
import django #
from django.core.asgi import get_asgi_application
from channels.routing import get_default_application #
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qrsocial_api.settings')
django.setup() #
# application = get_asgi_application()
application = get_default_application() #

# import os
# from django.urls import path
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# from django.core.asgi import get_asgi_application
# import chat.routing
# import user.routing
# from user.consumers import UserOnline
# from chat.consumers import ChatConsumer
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qrsocial_api.settings")
#
# application = ProtocolTypeRouter({
#     "http": get_asgi_application(),
#     'websocket': AuthMiddlewareStack(
#         URLRouter([
#             path('ws/user/online/', UserOnline.as_asgi()),
#             path('ws/chat/<chat_id>', ChatConsumer.as_asgi()),
#
#
#         ])
#     ),
# })
