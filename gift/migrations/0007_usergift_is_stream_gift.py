# Generated by Django 3.1.3 on 2020-12-10 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0006_gift_is_for_vip'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergift',
            name='is_stream_gift',
            field=models.BooleanField(default=False),
        ),
    ]