# Generated by Django 4.1.1 on 2022-10-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("results", "0002_alter_result_accord_alter_result_apc_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="result",
            name="remarks",
            field=models.TextField(blank=True, null=True),
        ),
    ]
