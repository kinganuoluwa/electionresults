# Generated by Django 4.1.1 on 2022-10-13 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("results", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pollingunit",
            name="polling_id",
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="pollingunit",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
