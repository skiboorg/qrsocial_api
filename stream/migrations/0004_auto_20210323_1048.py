# Generated by Django 3.1.3 on 2021-03-23 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stream', '0003_auto_20201210_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='stream',
            name='viewers',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='StreamLike',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='stream.stream')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
