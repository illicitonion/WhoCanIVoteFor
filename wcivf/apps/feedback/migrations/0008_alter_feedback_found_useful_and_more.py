# Generated by Django 4.2.11 on 2024-04-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("feedback", "0007_alter_feedback_token"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feedback",
            name="found_useful",
            field=models.CharField(
                blank=True,
                choices=[
                    ("YES", "Yes"),
                    ("NO", "No"),
                    ("PROBLEM", "Report a problem with this page"),
                ],
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="feedback",
            name="source_url",
            field=models.CharField(
                blank=True,
                default="https://whocanivotefor.co.uk",
                max_length=800,
            ),
        ),
        migrations.AlterField(
            model_name="feedback",
            name="vote",
            field=models.CharField(
                blank=True,
                choices=[
                    ("MORE_LIKELY", "More likely"),
                    ("LESS_LIKELY", "Less likely"),
                    ("NO_DIFFERENCE", "I always vote (no change)"),
                ],
                max_length=100,
            ),
        ),
    ]
