# Generated by Django 3.2.4 on 2023-02-19 09:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glavprofile',
            name='title',
            field=models.CharField(default='Пример профиля, который ты получишь после регистрации', max_length=53, validators=[django.core.validators.MinLengthValidator(40)], verbose_name='Мини-тайтл'),
        ),
    ]
