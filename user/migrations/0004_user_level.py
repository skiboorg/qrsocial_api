# Generated by Django 3.1.3 on 2020-11-26 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20201126_2042'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='level',
            field=models.IntegerField(default=0, verbose_name='Уровень'),
        ),
    ]
