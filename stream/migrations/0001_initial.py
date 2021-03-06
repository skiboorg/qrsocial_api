# Generated by Django 3.1.3 on 2020-12-10 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_vip', models.BooleanField(default=False)),
                ('is_private', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('stop', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='streams/')),
                ('uid', models.CharField(blank=True, max_length=255, null=True)),
                ('streamer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='streams', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
