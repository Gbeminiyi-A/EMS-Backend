from django.http import JsonResponse
from .models import Employee
from .models import Project
from .serializers import EmployeeSerializer
from .serializers import ProjectSerializer


def employeeList_view(request):
    # get all the drinks
    # serialize them
    # return json
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse({'employees': serializer.data}, )


def projectList_view(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return JsonResponse({'projects': serializer.data})
