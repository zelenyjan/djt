# Generated by Django 5.1.6 on 2025-02-17 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djt_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='photo'),
        ),
    ]
