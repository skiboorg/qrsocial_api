# Generated by Django 3.1.3 on 2020-12-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0004_donater'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='is_special_gift',
            field=models.BooleanField(default=False, verbose_name='Это подарок-запрос?'),
        ),
    ]