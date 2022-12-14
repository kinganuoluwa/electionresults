# Generated by Django 4.1.1 on 2022-10-13 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PollingUnit",
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
                (
                    "agent_first_name",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "agent_last_name",
                    models.CharField(blank=True, max_length=30, null=True),
                ),
                (
                    "agent_phone_number",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Ward",
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
                ("ward_number", models.PositiveIntegerField()),
                ("name", models.CharField(max_length=30)),
                (
                    "supervisor_first_name",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                (
                    "supervisor_phone_number",
                    models.PositiveBigIntegerField(blank=True, null=True),
                ),
                (
                    "supervisor_last_name",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Result",
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
                ("apc", models.IntegerField(default=0)),
                ("pdp", models.IntegerField(default=0)),
                ("accord", models.IntegerField(default=0)),
                ("remarks", models.TextField(blank=True, null=True)),
                (
                    "polling_unit",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="results.pollingunit",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="pollingunit",
            name="ward",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="results.ward"
            ),
        ),
    ]
