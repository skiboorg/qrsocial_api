# Generated by Django 3.1.3 on 2020-11-29 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20201129_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_show_at_home',
            field=models.BooleanField(default=False, verbose_name='Отображать стримера на главной?'),
        ),
    ]
