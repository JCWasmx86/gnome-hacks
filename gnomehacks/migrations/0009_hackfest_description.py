# Generated by Django 4.2.4 on 2023-09-03 18:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gnomehacks", "0008_alter_hackfest_end_alter_hackfest_start"),
    ]

    operations = [
        migrations.AddField(
            model_name="hackfest",
            name="description",
            field=models.TextField(
                default="",
                max_length=4194304,
                validators=[django.core.validators.MaxLengthValidator(4194304)],
            ),
            preserve_default=False,
        ),
    ]
