# Generated by Django 4.1.7 on 2023-04-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dev', '0005_startup_verify_team_verify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startup',
            name='verify',
            field=models.BooleanField(default=False, verbose_name='Галочка'),
        ),
        migrations.AlterField(
            model_name='team',
            name='verify',
            field=models.BooleanField(default=False, verbose_name='Галочка'),
        ),
    ]
