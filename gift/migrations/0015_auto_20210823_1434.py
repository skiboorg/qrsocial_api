# Generated by Django 3.1.3 on 2021-08-23 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0014_auto_20210823_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gift',
            name='is_with_answer',
        ),
        migrations.AddField(
            model_name='usergift',
            name='is_with_answer',
            field=models.BooleanField(default=False),
        ),
    ]
