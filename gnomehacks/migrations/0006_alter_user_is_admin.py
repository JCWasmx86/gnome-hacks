# Generated by Django 4.2.4 on 2023-09-03 17:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gnomehacks", "0005_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
    ]
