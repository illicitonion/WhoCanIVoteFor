# Generated by Django 3.2.12 on 2022-04-26 09:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("feedback", "0005_feedback_vote"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="flagged_as_spam",
            field=models.BooleanField(default=False),
        ),
    ]
