# Generated by Django 5.1.6 on 2025-02-20 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_jobcategory_jobinquiry_location_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.AddField(
            model_name='jobinquiry',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inquiries', to='jobs.job'),
        ),
        migrations.DeleteModel(
            name='SMSNotification',
        ),
    ]
