# Generated by Django 2.2.20 on 2021-04-19 13:32

from django.apps.registry import apps
from django.db import migrations


def delete_cvs(app, schema_editor):
    CV = apps.get_model("peoplecvs", "CV")
    CV.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("peoplecvs", "0002_auto_20170522_1324"),
    ]

    operations = [
        migrations.RunPython(
            code=delete_cvs, reverse_code=migrations.RunPython.noop
        )
    ]
