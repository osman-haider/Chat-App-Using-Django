# Generated by Django 5.0.2 on 2024-02-27 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatwithllm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='is_user',
            field=models.BooleanField(default=True),
        ),
    ]
