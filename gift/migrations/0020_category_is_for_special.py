# Generated by Django 3.1.3 on 2021-08-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0019_usergift_answer_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_for_special',
            field=models.BooleanField(default=False, verbose_name='Для спец подарков?'),
        ),
    ]