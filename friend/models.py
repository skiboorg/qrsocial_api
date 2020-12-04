from django.db import models


class FriendList(models.Model):
    user = models.ForeignKey('user.User',
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True,
                             verbose_name='Юзер',related_name='own_friend_list')

    friend_list = models.ManyToManyField('user.User',blank=True,
                                          verbose_name='Друзья'
                                          )

    def __str__(self):
        return f'Список друзей пользователя {self.user.email} | {self.user.nickname}'

    class Meta:
        verbose_name = "Список друзей"
        verbose_name_plural = "Список друзей"

class FriendApply(models.Model):
    user = models.ForeignKey('user.User',
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True,
                             verbose_name='Юзер')
    apply_list = models.ManyToManyField('user.User',
                                        verbose_name='Запросы в друзья',
                                        related_name='apply_list')

    def __str__(self):
        return f'Список заявок в друзья пользователя {self.user.email} | {self.user.nickname}'

    class Meta:
        verbose_name = "Список заявок в друзья"
        verbose_name_plural = "Список заявок в друзья"
