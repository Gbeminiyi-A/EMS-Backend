# Generated by Django 5.0.3 on 2024-03-27 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0017_rename_user_benefits_user_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 12, 52, 19, 36086, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 12, 52, 19, 36086, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 12, 52, 19, 36086, tzinfo=datetime.timezone.utc)),
        ),
    ]
