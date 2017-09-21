# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-21 01:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('promgen', '0040_default_farm'),
    ]

    operations = [
        migrations.AddField(
            model_name='sender',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
