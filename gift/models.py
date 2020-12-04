from django.db import models

class Gift(models.Model):
    name = models.CharField('Название подарка', max_length=255, blank=True, null=True)
    price = models.IntegerField('Цена', default=0)
    image = models.ImageField('Фото', upload_to='gifts/', blank=True, null=True)


class UserGift(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True, related_name='gifts')
    from_user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    message = models.CharField('Сообщение', max_length=255, blank=True, null=True)
