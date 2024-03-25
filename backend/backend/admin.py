from django.contrib import admin
from .models import Employee
from .models import Project

admin.site.register(Employee)
admin.site.register(Project)
