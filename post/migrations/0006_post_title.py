# Generated by Django 3.1.3 on 2021-08-23 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_is_vip'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
