from django.contrib import admin
from .models import Employee
from .models import Projects
from .models import Benefits
from .models import EmployeeLogin

admin.site.register(Employee)
admin.site.register(Projects)
admin.site.register(Benefits)
admin.site.register(EmployeeLogin)
