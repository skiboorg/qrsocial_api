# Generated by Django 3.1.3 on 2021-07-23 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20201128_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_vip',
            field=models.BooleanField(default=False),
        ),
    ]
