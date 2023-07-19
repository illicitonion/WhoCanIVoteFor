# Generated by Django 3.2 on 2021-09-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("people", "0038_add_party_name_to_personposts"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facebookadvert",
            name="ad_json",
            field=models.JSONField(
                help_text="The JSON returned from the Facebook Graph API for this advert"
            ),
        ),
        migrations.AlterField(
            model_name="personpost",
            name="elected",
            field=models.BooleanField(null=True),
        ),
    ]
