# Generated by Django 3.1.3 on 2021-08-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_video_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='gallery/video/', verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='video',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='gallery/video/image/', verbose_name='Фото'),
        ),
    ]