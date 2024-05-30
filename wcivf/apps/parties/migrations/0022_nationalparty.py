# Generated by Django 4.2.11 on 2024-06-03 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("elections", "0043_remove_election_ballot_papers_issued_and_more"),
        ("parties", "0021_party_nations"),
    ]

    operations = [
        migrations.CreateModel(
            name="NationalParty",
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
                ("name", models.CharField(blank=True, max_length=100)),
                ("facebook_page", models.URLField(blank=True, max_length=800)),
                ("instagram", models.URLField(blank=True, max_length=100)),
                ("homepage", models.URLField(blank=True, max_length=800)),
                ("email", models.EmailField(blank=True, max_length=254)),
                (
                    "youtube_profile_url",
                    models.URLField(blank=True, max_length=800),
                ),
                (
                    "contact_page_url",
                    models.URLField(blank=True, max_length=800),
                ),
                (
                    "party_political_broadcast",
                    models.URLField(blank=True, max_length=800),
                ),
                (
                    "file_url",
                    models.URLField(
                        blank=True,
                        help_text="The url to the google sheet the object was imported from. Not to be displayed.",
                        max_length=800,
                    ),
                ),
                (
                    "is_national",
                    models.BooleanField(
                        default=True,
                        help_text="Used to identify if obj is related to a national election",
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="general_election_parties",
                        to="parties.party",
                    ),
                ),
                (
                    "post_election",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="elections.postelection",
                    ),
                ),
            ],
        ),
    ]
