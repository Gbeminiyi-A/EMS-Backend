from rest_framework import serializers
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'gender', 'marital_status', 'highest_education', 'skills', 'manager', 'date_joined']
