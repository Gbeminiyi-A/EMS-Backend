from rest_framework import serializers
from .models import Employee
from .models import Projects
from .models import Benefits


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phone_number', 'gender', 'highest_education', 'marital_status', 'skills',
                  'manager', 'date_joined', 'designation']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['assigned_employee', 'project_id', 'project_name', 'project_domain', 'project_description', 'project_role',
                  'client_name', 'required_resources', 'budget', 'project_manager', 'start_date', 'end_date']


class BenefitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Benefits
        fields = ['user_id', 'basic_salary', 'hra_allowance', 'additional_allowance', 'professional_tax', 'medical_premium',
                  'income_tax', 'pf_deductions', 'gross_earning', 'gross_deduction']
