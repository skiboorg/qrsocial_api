from django.db import models



class Category(models.Model):
    order_num = models.IntegerField(default=100)
    name = models.CharField('Название', max_length=255, blank=True, null=True)
    icon = models.ImageField('Иконка', upload_to='gifts/', blank=True, null=True)
    is_for_vip = models.BooleanField('Для VIP?', default=False)
    is_for_special = models.BooleanField('Для спец подарков?', default=False)

    class Meta:
        ordering = ('order_num',)


class Gift(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='gifts', blank=True, null=True)
    name = models.CharField('Название подарка', max_length=255, blank=True, null=True)
    price = models.IntegerField('Цена', default=0)
    image = models.ImageField('Фото', upload_to='gifts/', blank=True, null=True)
    is_special_gift = models.BooleanField('Это подарок-запрос?',default=False)
    is_for_vip = models.BooleanField('Для VIP?',default=False)

    description = models.TextField('Описание', blank=True, null=True)


class UserGift(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True, related_name='gifts')
    from_user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_stream_gift = models.BooleanField(default=False)
    is_with_answer = models.BooleanField(default=False)
    message = models.CharField('Сообщение', max_length=255, blank=True, null=True)
    answer_text = models.TextField(blank=True,null=True)
    answer_file = models.FileField(upload_to='gifts_files/',blank=True,null=True)
    answer_date = models.DateTimeField(auto_now=True, blank=False, null=True)

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



class TotalDonates(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, null=True, blank=True)
    summ = models.IntegerField(default=0)



