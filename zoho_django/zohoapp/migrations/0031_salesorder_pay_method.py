# Generated by Django 4.2.3 on 2023-10-08 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zohoapp", "0030_salesorder_balance"),
    ]

    operations = [
        migrations.AddField(
            model_name="salesorder",
            name="pay_method",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
