from django.db import models


class FeedBackForm(models.Model):
    name = models.CharField('От', max_length=255, blank=False,null=True)
    email = models.EmailField('Email', blank=False, null=True)
    text = models.TextField('Email', blank=True, null=True)
    phone = models.CharField('Телефон', max_length=255, blank=True, null=True)
    created_at = models.DateField('Создана', auto_now_add=True)

    def __str__(self):
        return f'Форма обратной связи от {self.name} | {self.email}'

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"