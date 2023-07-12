# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-26 14:48
from __future__ import unicode_literals

from django.db import migrations


def add_site(apps, schema_editor):
    Site = apps.get_model("sites", "Site")

    site = Site(
        pk=1, name="whocanivotefor.co.uk", domain="whocanivotefor.co.uk"
    )
    site.save()


class Migration(migrations.Migration):
    dependencies = [("core", "0001_initial"), ("sites", "0001_initial")]

    operations = [migrations.RunPython(add_site)]
