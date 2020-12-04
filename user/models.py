from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from friend.models import *
from .services import *
import uuid

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, wechatid, password, **extra_fields):
        user = self.model( wechatid=wechatid, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, wechatid, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(wechatid, password, **extra_fields)

    def create_superuser(self, wechatid, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(wechatid, password, **extra_fields)


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    avatar = models.ImageField('Фото', upload_to='user/avatars',blank=True,null=True)
    bg_image = models.ImageField('Задний фон', upload_to='user/bg',blank=True,null=True)
    fio = models.CharField('ФИО', max_length=50, blank=True, null=True, default='John Doe')
    nickname = models.CharField('@ник', max_length=50, blank=True, null=True, unique=True)
    wechatid = models.CharField('wechatid', max_length=50, blank=True, null=True, unique=True)
    email = models.EmailField('Эл. почта', blank=True, null=True, unique=True)
    birthday = models.DateField('День рождения', blank=True, null=True)

    balance = models.IntegerField('Баланс', default=0)
    rating = models.IntegerField('Рейтинг чувака', default=1)
    streamer_rating = models.IntegerField('Рейтинг бабы', default=1)
    streams_rating = models.IntegerField('Рейтинг стримов', default=1)
    level = models.IntegerField('Уровень', default=1)
    years = models.IntegerField('Лет', default=0)

    vip_update = models.DateField('Дата начала аккаунта', blank=True, null=True)
    vip_expire = models.DateField('Дата завершения аккаунта', blank=True, null=True)
    last_online = models.DateTimeField('Последний раз был онлайн', auto_now=True, null=True)

    is_vip = models.BooleanField('VIP?', default=False)
    is_streamer = models.BooleanField('Стример?', default=False)
    is_online = models.BooleanField('Онлайн?', default=False)
    is_verified = models.BooleanField('Акканнт подтвержден?', default=False)
    is_email_verified = models.BooleanField('EMail подтвержден?', default=False)
    is_show_at_home = models.BooleanField('Отображать стримера на главной?', default=False)

    verify_code = models.CharField('Код подтверждения', max_length=50, blank=True, null=True)
    stream_key = models.UUIDField('Ключ стрима',blank=True,null=True, default=uuid.uuid4)
    channel = models.CharField(max_length=255,blank=True,null=True)

    USERNAME_FIELD = 'wechatid'
    REQUIRED_FIELDS = []

    objects = UserManager()

    # def __str__(self):
    #     if self.phone:
    #         return f'{self.get_full_name()} {self.phone}'
    #     elif self.email:
    #         return f'{self.get_full_name()} {self.email}'
    #     else:
    #         return f'{self.get_full_name()} {self.id}'
    #
    # def get_user_activity(self):
    #     if (timezone.now() - self.last_activity) > dt.timedelta(seconds=10):
    #         return f'Был {self.last_activity.strftime("%d.%m.%Y,%H:%M:%S")}'
    #     else:
    #         return 'В сети'
    #
    #
    # def get_rating(self):
    #     try:
    #         return round(self.rating / self.rate_times)
    #     except:
    #         return 0

    def get_full_name(self):
        if self.is_person:
            if self.first_name and self.last_name:
                return f'{self.first_name} {self.last_name}'
            elif self.first_name and not self.last_name:
                return f'{self.first_name}'
            elif not self.first_name and not self.last_name:
                return 'Неизвестный пользователь'
        else:
            return f'{self.organization_name}'


    # def get_avatar(self):
    #     if self.avatar:
    #         return self.avatar.url
    #     else:
    #         return '/static/img/no_ava.jpg'



def user_post_save(sender, instance, created, **kwargs):
    """Создание всех значений по-умолчанию для нового пользовыателя"""

    if created:
        FriendList.objects.create(user=instance)
        FriendApply.objects.create(user=instance)


post_save.connect(user_post_save, sender=User)
