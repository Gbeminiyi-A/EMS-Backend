# Generated by Django 5.0.3 on 2024-03-27 11:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_benefits_remove_employee_additional_allowance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 11, 42, 14, 2727, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 11, 42, 14, 2727, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 11, 42, 14, 2727, tzinfo=datetime.timezone.utc)),
        ),
    ]
