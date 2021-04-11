from django.contrib import admin
from .models import *
admin.site.register(User)
admin.site.register(UserTag)
admin.site.register(UserBg)
admin.site.register(BgGroup)

