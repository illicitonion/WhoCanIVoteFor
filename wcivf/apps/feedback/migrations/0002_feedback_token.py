# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-29 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("feedback", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="token",
            field=models.CharField(blank=True, max_length=100),
        )
    ]
