# Generated by Django 4.1.5 on 2023-01-12 00:26

from decimal import Decimal
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("subscriptionmanager", "0001_schema"),
    ]

    operations = [
        migrations.CreateModel(
            name="ChangeSummary",
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
                ("last_synced", models.DateTimeField()),
                ("subscription_guid", models.UUIDField()),
                ("customer_name", models.CharField(max_length=200)),
                (
                    "customer_account_number",
                    models.CharField(max_length=50, unique=True),
                ),
                ("currency", models.CharField(max_length=3)),
                ("change_type", models.TextField()),
                ("date", models.DateField()),
                ("note", models.TextField(blank=True)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("salesperson", models.CharField(max_length=200)),
            ],
            options={
                "db_table": 'subscriptionmanager"."billing_change_summary',
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="ChargeSummary",
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
                ("last_synced", models.DateTimeField()),
                ("created", models.DateTimeField()),
                ("updated", models.DateTimeField()),
                ("requestor", models.CharField(max_length=200)),
                ("subscription_guid", models.UUIDField()),
                ("customer_name", models.CharField(max_length=200)),
                (
                    "customer_account_number",
                    models.CharField(max_length=50, unique=True),
                ),
                ("currency", models.CharField(max_length=3)),
                ("itemcode", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=500)),
                ("account_code", models.CharField(max_length=20)),
                ("quantity", models.DecimalField(decimal_places=2, max_digits=10)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("tracking_category_1", models.CharField(max_length=50)),
                ("tracking_category_2", models.CharField(max_length=50)),
                ("subtotal", models.DecimalField(decimal_places=2, max_digits=10)),
                ("total", models.DecimalField(decimal_places=2, max_digits=10)),
                ("invoice_date", models.DateField(null=True)),
                ("invoice_reference", models.CharField(max_length=20, null=True)),
                ("invoice_number", models.CharField(max_length=20, null=True)),
            ],
            options={
                "db_table": 'subscriptionmanager"."billing_charge_summary',
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="PaymentMethodSummary",
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
                ("last_synced", models.DateTimeField()),
                ("customer_account_number", models.CharField(max_length=50)),
                ("gocardless_id", models.CharField(max_length=100)),
                ("stripe_id", models.CharField(max_length=100)),
                ("description", models.CharField(blank=True, max_length=250)),
            ],
            options={
                "db_table": 'subscriptionmanager"."billing_paymentmethod_summary',
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="RecurringCreditSummary",
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
                ("last_synced", models.DateTimeField()),
                ("subscription_guid", models.UUIDField()),
                ("customer_name", models.CharField(max_length=200)),
                (
                    "customer_account_number",
                    models.CharField(max_length=50, unique=True),
                ),
                ("currency", models.CharField(max_length=3)),
                ("start_date", models.DateField()),
                ("review_date", models.DateField(blank=True, null=True)),
                ("expiry_date", models.DateField()),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("invoice_text", models.CharField(max_length=200)),
                ("internal_note", models.CharField(blank=True, max_length=500)),
                ("credit_classification", models.TextField()),
            ],
            options={
                "db_table": 'subscriptionmanager"."billing_recurring_credit_summary',
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="RevenueForecastSummary",
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
                ("last_synced", models.DateTimeField()),
                ("month", models.DateField()),
                (
                    "total_contract_value",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "total_credit_value",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("signed_value", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "starting_value",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("subs_total", models.IntegerField()),
                ("subs_total_paying", models.IntegerField()),
                ("subs_starting", models.IntegerField()),
                ("subs_won", models.IntegerField()),
                ("subs_lost", models.IntegerField()),
            ],
            options={
                "db_table": 'subscriptionmanager"."billing_revenueforecast_summary',
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="SubscriptionSummary",
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
                ("last_synced", models.DateTimeField()),
                ("created", models.DateTimeField()),
                ("updated", models.DateTimeField()),
                ("salesperson", models.CharField(max_length=200)),
                ("product", models.CharField(max_length=200)),
                ("customer_name", models.CharField(max_length=200)),
                (
                    "customer_account_number",
                    models.CharField(max_length=50, unique=True),
                ),
                ("customer_xero_guid", models.UUIDField(blank=True)),
                ("customer_primary_contact_name", models.CharField(max_length=200)),
                ("customer_primary_contact_email", models.CharField(max_length=200)),
                ("customer_accounts_contact_name", models.CharField(max_length=200)),
                ("customer_accounts_contact_email", models.CharField(max_length=200)),
                (
                    "customer_company_tax_number",
                    models.CharField(
                        help_text="ABN, NZBN or VAT number.", max_length=50
                    ),
                ),
                ("subscription_guid", models.UUIDField()),
                ("currency", models.CharField(max_length=3)),
                ("signing_date", models.DateField()),
                ("billing_date", models.DateField()),
                ("plan", models.CharField(max_length=100)),
                ("staff_addon_name", models.CharField(max_length=100)),
                ("plan_included_licenses", models.IntegerField(blank=True, null=True)),
                (
                    "additional_committed_staff",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "total_contracted_staff_licenses",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "override_plan_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "override_staff_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "effective_discount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "total_contract_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "hosting_addon_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "bi_addon_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "sla_addon_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "workspaces",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=50),
                        blank=True,
                        default=list,
                        size=None,
                    ),
                ),
                ("termination_date", models.DateField(blank=True, null=True)),
                ("termination_code", models.TextField(blank=True)),
                ("termination_reason", models.TextField(blank=True)),
                (
                    "current_expansion_chargeable",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "current_total_mrr_chargeable",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "current_total_used_staff_licenses",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "current_total_additional_chargable_licenses",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "current_monthly_recurring_credit",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "lastmonth_expansion_charged",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "lastmonth_total_mrr_charged",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "lastmonth_total_used_staff_licenses",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "lastmonth_total_used_desk_licenses",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "lastmonth_total_used_field_licenses",
                    models.IntegerField(blank=True, null=True),
                ),
                (
                    "lastmonth_total_additional_chargable_licenses",
                    models.IntegerField(blank=True, null=True),
                ),
            ],
            options={
                "db_table": 'subscriptionmanager"."billing_subscription_summary',
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="WorkspaceSummary",
            fields=[
                ("last_synced", models.DateTimeField()),
                ("guid", models.UUIDField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "customer_account_number",
                    models.CharField(max_length=50, unique=True),
                ),
                ("subscription_guid", models.UUIDField()),
            ],
            options={
                "db_table": 'subscriptionmanager"."billing_workspace_summary',
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="XeroContactSummary",
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
                ("last_synced", models.DateTimeField()),
                ("customer_name", models.CharField(max_length=200)),
                ("customer_account_number", models.CharField(max_length=50)),
                ("customer_first_name", models.CharField(max_length=100)),
                ("customer_last_name", models.CharField(max_length=100)),
            ],
            options={
                "db_table": 'subscriptionmanager"."billing_xero_customer_summary',
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="XeroInvoiceSummary",
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
                ("last_synced", models.DateTimeField()),
                ("invoice_guid", models.UUIDField()),
                ("contact_guid", models.UUIDField()),
                ("contact_name", models.CharField(max_length=200)),
                ("contact_account_number", models.CharField(max_length=50)),
                ("number", models.CharField(max_length=50)),
                ("reference", models.CharField(max_length=100)),
                ("date", models.DateField(blank=True, null=True)),
                ("due_date", models.DateField(blank=True, null=True)),
                (
                    "subtotal",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0.00"), max_digits=10
                    ),
                ),
                (
                    "total",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0.00"), max_digits=10
                    ),
                ),
                ("status", models.CharField(max_length=50)),
                ("currency", models.CharField(max_length=3)),
                (
                    "currency_rate",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0.00"), max_digits=10
                    ),
                ),
                ("is_sent", models.BooleanField()),
                ("repeating_invoice_guid", models.UUIDField()),
                (
                    "amount_due",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0.00"), max_digits=10
                    ),
                ),
                (
                    "amount_paid",
                    models.DecimalField(
                        decimal_places=2, default=Decimal("0.00"), max_digits=10
                    ),
                ),
                ("fully_paid_on_date", models.DateField(blank=True, null=True)),
            ],
            options={
                "db_table": 'subscriptionmanager"."billing_xero_invoice_summary',
                "default_permissions": (),
            },
        ),
    ]
