# Generated by Django 3.1.3 on 2020-11-28 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20201128_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postlike',
            old_name='liked_users',
            new_name='users',
        ),
    ]
