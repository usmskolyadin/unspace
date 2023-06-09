# Generated by Django 4.1.7 on 2023-03-31 07:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='ITUtopies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Название')),
                ('full_text', models.TextField(max_length=2000, validators=[django.core.validators.MinLengthValidator(100)], verbose_name='Айтиутопия')),
                ('code', models.TextField(verbose_name='Код')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('project', models.TextField(max_length=20, verbose_name='Проект')),
                ('slug', models.SlugField(allow_unicode=True, default=uuid.uuid4, max_length=255, verbose_name='URL')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Айтиутопия',
                'verbose_name_plural': 'Айтиутопии',
            },
        ),
        migrations.CreateModel(
            name='ITUtopiaComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(10)])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('itopia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='itutopies.itutopies')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
