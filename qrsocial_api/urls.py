from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/v1/user/', include('user.urls')),
    path('api/v1/post/', include('post.urls')),
    path('api/v1/gallery/', include('gallery.urls')),
    path('api/v1/chat/', include('chat.urls')),
    path('api/v1/friend/', include('friend.urls')),
    path('api/v1/gift/', include('gift.urls')),
    path('api/v1/stream/', include('stream.urls')),
    path('api/v1/feedback/', include('feedback.urls')),
    path('api/v1/blog/', include('blog.urls')),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
