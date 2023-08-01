# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 19:44
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("people", "0025_personpost_post_election")]

    operations = [
        migrations.AlterField(
            model_name="personpost",
            name="post_election",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="elections.PostElection",
            ),
        )
    ]
