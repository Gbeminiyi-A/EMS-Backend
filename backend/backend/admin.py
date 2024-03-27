from django.contrib import admin
from .models import Employee
from .models import Project
from .models import Benefits

admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Benefits)
