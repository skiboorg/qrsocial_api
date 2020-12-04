from django.db import models

class UserHistory(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, blank=True, null=True)
    action = models.CharField('Действие', max_length=50, blank=True, null=True)
