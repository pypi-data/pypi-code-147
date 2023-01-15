# Generated by Django 1.10 on 2017-05-21 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("request_token", "0008_convert_token_data_to_jsonfield")]

    operations = [
        migrations.CreateModel(
            name="RequestTokenErrorLog",
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
                (
                    "error_type",
                    models.CharField(
                        help_text="The underlying type of error raised.", max_length=50
                    ),
                ),
                (
                    "error_message",
                    models.CharField(
                        help_text="The error message supplied.", max_length=200
                    ),
                ),
                (
                    "log",
                    models.OneToOneField(
                        help_text="The token use against which the error occurred.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="error",
                        to="request_token.RequestTokenLog",
                    ),
                ),
                (
                    "token",
                    models.ForeignKey(
                        help_text="The RequestToken that was used.",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="errors",
                        to="request_token.RequestToken",
                    ),
                ),
            ],
        )
    ]
