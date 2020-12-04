from .models import *

def create_user_history(user,action):
    UserHistory.objects.create(user=user, action=action)
