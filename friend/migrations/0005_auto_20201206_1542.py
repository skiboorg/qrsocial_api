# Generated by Django 3.1.3 on 2020-12-06 12:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('friend', '0004_auto_20201129_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendlist',
            name='friend_list',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Друзья'),
        ),
    ]
