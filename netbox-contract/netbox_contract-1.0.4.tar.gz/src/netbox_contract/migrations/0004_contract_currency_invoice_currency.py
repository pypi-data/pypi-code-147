# Generated by Django 4.1.5 on 2023-01-15 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_contract", "0003_alter_contract_custom_field_data_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contract",
            name="currency",
            field=models.CharField(default="usd", max_length=3),
        ),
        migrations.AddField(
            model_name="invoice",
            name="currency",
            field=models.CharField(default="usd", max_length=3),
        ),
    ]
