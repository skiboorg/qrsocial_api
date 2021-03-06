# Generated by Django 3.1.3 on 2020-11-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='orders_count',
        ),
        migrations.RemoveField(
            model_name='user',
            name='partner_balance',
        ),
        migrations.RemoveField(
            model_name='user',
            name='rent_count',
        ),
        migrations.AlterField(
            model_name='user',
            name='fio',
            field=models.CharField(blank=True, default='John Doe', max_length=50, null=True, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='@ник'),
        ),
    ]
