# Generated by Django 3.1.3 on 2020-12-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0001_initial'),
        ('user', '0006_user_is_show_at_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gifts',
            field=models.ManyToManyField(blank=True, to='gift.Gift'),
        ),
        migrations.AddField(
            model_name='user',
            name='streamer_rating',
            field=models.IntegerField(default=1, verbose_name='Рейтинг бабы'),
        ),
        migrations.AddField(
            model_name='user',
            name='streams_rating',
            field=models.IntegerField(default=1, verbose_name='Рейтинг стримов'),
        ),
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.IntegerField(default=1, verbose_name='Рейтинг чувака'),
        ),
    ]
