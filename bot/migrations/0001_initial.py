# Generated by Django 4.0.1 on 2022-11-08 12:44

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
            name='TgUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.BigIntegerField(unique=True, verbose_name=' TG Chat ID')),
                ('username', models.CharField(blank=True, default=None, max_length=255, unique=True, verbose_name='TG username')),
                ('verification_code', models.CharField(blank=True, default=None, max_length=100, unique=True)),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Телеграм Пользователь',
                'verbose_name_plural': 'Телеграмм Пользователи',
            },
        ),
    ]
