# Generated by Django 5.1 on 2024-09-17 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userfiles',
            name='cleaned',
            field=models.BooleanField(default=False, verbose_name='Cleaned'),
        ),
    ]
