# Generated by Django 3.1.3 on 2020-12-10 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='is_acrhived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stream',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
