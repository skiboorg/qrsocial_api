from django.db import models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
channel_layer = get_channel_layer()

class TraslateKey(models.Model):
    key = models.CharField(max_length=255,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class StikerGroup(models.Model):
    name = models.CharField('Название группы', max_length=255, blank=False, null=True)
    is_for_vip = models.BooleanField('Для VIP?', default=False)
    is_for_vip_level = models.IntegerField('Для ВИП уровня', default=1)

    def __str__(self):
        return f'Группа стикеров {self.name} | Для ВИП :{self.is_for_vip}'

    class Meta:
        verbose_name = "Группа стикеров"
        verbose_name_plural = "Группы стикеров"

class Stiker(models.Model):
    group = models.ForeignKey(StikerGroup, on_delete=models.CASCADE, null=True, blank=False, related_name='stikers')
    image = models.ImageField('Изображение', upload_to='chat/', blank=True, null=True)

    def __str__(self):
        return f'Cтикер в группе :{self.group.name}'

    class Meta:
        verbose_name = "Стикер"
        verbose_name_plural = "Стикеры"

class Chat(models.Model):
    users = models.ManyToManyField('user.User', blank=True,  verbose_name='Пользователи',
                                    related_name='chatusers',db_index=True)
    starter = models.ForeignKey('user.User',blank=True,null=True,on_delete=models.CASCADE,related_name='starter')
    opponent = models.ForeignKey('user.User',blank=True,null=True,on_delete=models.CASCADE,related_name='opponent')
    stream = models.ForeignKey('stream.Stream',blank=True,null=True,on_delete=models.CASCADE,related_name='stream_chat')
    isNewMessages = models.BooleanField('Есть новые сообщения', default=False)
    lastMessageOwn = models.BooleanField( default=False)
    is_stream_chat = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def get_last_message_text(self):
        try:
            return self.messages.last().message
        except:
            return ''

    def get_last_message_user_status(self):
        try:
            return True if self.messages.last().user.is_online else False
        except:
            return False

    def get_last_message_user_avatar(self):
        try:
            return self.messages.last().user.avatar.url
        except:
            return 'no_ava'

    def get_last_message_user_id(self):
        try:
            return self.messages.last().user.id
        except:
            return ''

    def get_last_message_user_name(self):
        try:
            return self.messages.last().user.get_full_name()
        except:
            return ''


class Message(models.Model):
    chat = models.ForeignKey(Chat, blank=False, null=True, on_delete=models.CASCADE, verbose_name='В чате',
                             related_name='messages',db_index=True)
    user = models.ForeignKey('user.User', blank=False, null=True, on_delete=models.CASCADE, verbose_name='Сообщение от')
    stiker = models.ForeignKey(Stiker, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Стикер')
    message = models.TextField('Сообщение', blank=True,null=True)
    message_translate = models.TextField('Перевод', blank=True,null=True)
    image = models.ImageField('Изображение к сообщению', upload_to='chat/', blank=True, null=True)
    isUnread = models.BooleanField('Не прочитанное сообщение', default=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.isUnread:
            self.chat.isNewMessages = True
            self.chat.save()

        super(Message, self).save(*args, **kwargs)


