# Generated by Django 2.2.7 on 2019-12-13 10:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("people", "0035_personpost_votes_cast")]

    operations = [
        migrations.AlterField(
            model_name="personpost",
            name="votes_cast",
            field=models.PositiveIntegerField(null=True),
        )
    ]
