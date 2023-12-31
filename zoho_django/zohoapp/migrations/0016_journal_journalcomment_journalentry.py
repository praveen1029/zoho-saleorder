# Generated by Django 3.2.20 on 2023-09-25 12:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0015_auto_20230925_1023'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('journal_no', models.CharField(max_length=255, unique=True)),
                ('reference_no', models.CharField(blank=True, max_length=255)),
                ('notes', models.TextField(blank=True)),
                ('currency', models.CharField(max_length=255)),
                ('cash_journal', models.BooleanField(default=False)),
                ('attachment', models.FileField(blank=True, upload_to='attachments/')),
                ('total_debit', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_credit', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('difference', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('contact', models.CharField(max_length=200)),
                ('debits', models.DecimalField(decimal_places=2, max_digits=10)),
                ('credits', models.DecimalField(decimal_places=2, max_digits=10)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.journal')),
            ],
        ),
        migrations.CreateModel(
            name='JournalComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='zohoapp.journal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
