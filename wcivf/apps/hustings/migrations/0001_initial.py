# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-14 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [("elections", "0016_postelection_contested")]

    operations = [
        migrations.CreateModel(
            name="Husting",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=250)),
                ("url", models.URLField()),
                ("starts", models.DateTimeField()),
                ("ends", models.DateTimeField(blank=True, null=True)),
                (
                    "location",
                    models.CharField(blank=True, max_length=250, null=True),
                ),
                (
                    "postcode",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
                (
                    "post_election",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="elections.PostElection",
                    ),
                ),
            ],
        )
    ]
