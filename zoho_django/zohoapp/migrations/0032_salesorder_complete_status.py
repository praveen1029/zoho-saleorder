# Generated by Django 4.2.3 on 2023-10-09 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zohoapp", "0031_salesorder_pay_method"),
    ]

    operations = [
        migrations.AddField(
            model_name="salesorder",
            name="complete_status",
            field=models.IntegerField(default=0),
        ),
    ]
