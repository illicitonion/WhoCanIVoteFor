# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-21 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("elections", "0022_auto_20181031_1603")]

    operations = [
        migrations.AddField(
            model_name="election",
            name="any_non_by_elections",
            field=models.BooleanField(default=False),
            preserve_default=False,
        )
    ]
