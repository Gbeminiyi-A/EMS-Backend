# Generated by Django 5.0.3 on 2024-03-27 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_alter_employee_date_joined_alter_projects_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 13, 5, 59, 716721, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 13, 5, 59, 717708, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project',
            field=models.ManyToManyField(blank=True, to='backend.employee'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='project_domain',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 13, 5, 59, 717708, tzinfo=datetime.timezone.utc)),
        ),
    ]
