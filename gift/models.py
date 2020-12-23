from django.db import models

class Gift(models.Model):
    name = models.CharField('Название подарка', max_length=255, blank=True, null=True)
    price = models.IntegerField('Цена', default=0)
    image = models.ImageField('Фото', upload_to='gifts/', blank=True, null=True)
    is_special_gift = models.BooleanField('Это подарок-запрос?',default=False)
    is_for_vip = models.BooleanField('Для VIP?',default=False)
    description = models.TextField('Описание',blank=True,null=True)


class UserGift(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True, related_name='gifts')
    from_user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    is_stream_gift = models.BooleanField(default=False)
    message = models.CharField('Сообщение', max_length=255, blank=True, null=True)

class Donater(models.Model):
    to_user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True,related_name='to_user')
    from_user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True,related_name='from_user')
    summ = models.IntegerField(default=0)


class StreamDonater(models.Model):
    stream = models.ForeignKey('stream.Stream', on_delete=models.CASCADE, null=True, blank=True)
    to_user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True,
                                related_name='stream_to_user')
    from_user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True,
                                  related_name='stream_from_user')
    summ = models.IntegerField(default=0)
