# Generated by Django 3.1.3 on 2020-12-10 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0005_gift_is_special_gift'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='is_for_vip',
            field=models.BooleanField(default=False, verbose_name='Для VIP?'),
        ),
    ]
