# Generated by Django 2.0.1 on 2018-07-28 15:20

import chat.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20180725_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatsession',
            name='uri',
            field=models.CharField(default=chat.models._generate_unique_uri, max_length=200, unique=True),
        ),
    ]
