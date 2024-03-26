from django.http import JsonResponse
from .models import Employee
from .models import Project
from .serializers import EmployeeSerializer
from .serializers import ProjectSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def employeeList_view(request):
    # get all the drinks
    # serialize them
    # return json
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse({'employees': serializer.data}, )
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'employees': serializer.data})


def projectList_view(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return JsonResponse({'projects': serializer.data})
