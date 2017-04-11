# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-11 01:32
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('volunteers', '0003_volunteerhours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerhours',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
