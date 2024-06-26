# Generated by Django 5.0.3 on 2024-03-27 11:33

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_alter_employee_date_joined_alter_project_end_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='backend.employee')),
                ('basic_salary', models.DecimalField(decimal_places=3, default=0, max_digits=200)),
                ('hra_allowance', models.DecimalField(decimal_places=3, default=0, max_digits=200)),
                ('additional_allowance', models.DecimalField(decimal_places=3, default=0, max_digits=200)),
                ('professional_tax', models.DecimalField(decimal_places=3, default=0, max_digits=200)),
                ('medical_premium', models.DecimalField(decimal_places=3, default=0, max_digits=200)),
                ('income_tax', models.DecimalField(decimal_places=3, default=0, max_digits=200)),
                ('pf_deductions', models.DecimalField(decimal_places=3, default=0, max_digits=200)),
                ('gross_earning', models.DecimalField(decimal_places=3, default=0, max_digits=200)),
                ('gross_deduction', models.DecimalField(decimal_places=3, default=0, max_digits=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='additional_allowance',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='basic_salary',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='gross_deduction',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='gross_earning',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='hra_allowance',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='income_tax',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='medical_premium',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='pf_deductions',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='professional_tax',
        ),
        migrations.AddField(
            model_name='employee',
            name='designation',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(default='@gmail.com', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 11, 33, 1, 137023, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 11, 33, 1, 137023, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 27, 11, 33, 1, 137023, tzinfo=datetime.timezone.utc)),
        ),
    ]
