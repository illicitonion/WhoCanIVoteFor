# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-22 12:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("parties", "0007_auto_20180417_1733")]

    operations = [
        migrations.AlterField(
            model_name="manifesto",
            name="pdf_url",
            field=models.URLField(blank=True, max_length=800),
        ),
        migrations.AlterField(
            model_name="manifesto",
            name="web_url",
            field=models.URLField(blank=True, max_length=800),
        ),
    ]
