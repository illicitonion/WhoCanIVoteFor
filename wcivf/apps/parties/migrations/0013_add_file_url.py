# Generated by Django 3.2.12 on 2022-04-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("parties", "0012_add_youtube_and_contact_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="localparty",
            name="file_url",
            field=models.URLField(
                blank=True,
                help_text="The url to the google sheet the object was imported from. Not to be displayed.",
                max_length=800,
            ),
        ),
        migrations.AddField(
            model_name="manifesto",
            name="file_url",
            field=models.URLField(
                blank=True,
                help_text="The url to the google sheet the object was imported from. Not to be displayed.",
                max_length=800,
            ),
        ),
    ]
