# Generated by Django 4.1.7 on 2023-04-20 17:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regauth', '0003_alter_profile_verify'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='git',
            field=models.URLField(default=1, verbose_name='GitHub пользователя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='telegram',
            field=models.URLField(default=1, verbose_name='Телеграм пользователя'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='vk',
            field=models.URLField(default=1, verbose_name='Вконтакте пользователя'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, default='Добро пожаловать на UnrealSpace! Пожалуйста, заполните свой профиль. ', max_length=100, validators=[django.core.validators.MinLengthValidator(50)]),
        ),
    ]
