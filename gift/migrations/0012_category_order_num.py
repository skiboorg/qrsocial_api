# Generated by Django 3.1.3 on 2021-08-23 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0011_auto_20210812_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order_num',
            field=models.IntegerField(default=100),
        ),
    ]
