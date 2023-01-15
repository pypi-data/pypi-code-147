# Generated by Django 4.1.5 on 2023-01-15 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("netbox_contract", "0004_contract_currency_invoice_currency"),
    ]

    operations = [
        migrations.AddField(
            model_name="contract",
            name="accounting_dimensions",
            field=models.JSONField(null=True),
        ),
        migrations.AddField(
            model_name="invoice",
            name="accounting_dimensions",
            field=models.JSONField(null=True),
        ),
    ]
