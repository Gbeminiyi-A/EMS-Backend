from django.http import JsonResponse
from .models import Employee
from .serializers import EmployeeSerializer


def employeeList_view(request):
    # get all the drinks
    # serialize them
    # return json
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return JsonResponse(serializer.data, safe=False)
