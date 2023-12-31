# Generated by Django 4.2.4 on 2023-09-03 15:00

import django.db.models.deletion
from django.db import migrations, models

import gnomehacks.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=1073741824)),
                ("name", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=200)),
                ("country", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("email", models.CharField(max_length=200)),
                ("is_admin", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Hackfest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("question_text", models.CharField(max_length=200)),
                (
                    "attendees",
                    models.JSONField(
                        default=gnomehacks.models.empty_array, verbose_name="Attendees"
                    ),
                ),
                (
                    "trusted_users",
                    models.JSONField(
                        default=gnomehacks.models.empty_array,
                        verbose_name="Trusted Users",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="gnomehacks.location",
                    ),
                ),
            ],
        ),
    ]
