# Generated by Django 5.0.3 on 2024-03-25 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_project_end_date_alter_project_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]