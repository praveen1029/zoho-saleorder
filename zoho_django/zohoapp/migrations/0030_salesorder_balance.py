# Generated by Django 4.2.3 on 2023-10-08 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zohoapp", "0029_alter_salesorder_adjust"),
    ]

    operations = [
        migrations.AddField(
            model_name="salesorder",
            name="balance",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
