# Generated by Django 3.1.3 on 2021-01-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBackForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='От')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Email')),
                ('text', models.TextField(null=True, verbose_name='Email')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Создана')),
            ],
            options={
                'verbose_name': 'Форма обратной связи',
                'verbose_name_plural': 'Формы обратной связи',
            },
        ),
    ]