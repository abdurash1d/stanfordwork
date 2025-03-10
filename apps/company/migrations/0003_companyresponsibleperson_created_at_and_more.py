# Generated by Django 5.1.3 on 2025-01-21 13:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_remove_company_responsible_person_company_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyresponsibleperson',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='companyresponsibleperson',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='companyresponsibleperson',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
