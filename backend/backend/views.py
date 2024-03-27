from django.http import JsonResponse
from .models import Employee
from .models import Projects
from .models import Benefits
from .serializers import EmployeeSerializer
from .serializers import ProjectSerializer
from .serializers import BenefitsSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response


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


@api_view(['GET', 'POST'])
def projectList_view(request):
    projects = Projects.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return JsonResponse({'projects': serializer.data})


@api_view(['GET', 'PUT', 'DELETE'])
def projectDetail_view(request, project_id):
    """ Use product id to get the details of the project. If by any chance two projects have the same project id(
    which should not be possible) only the first project in the db is edited and or deleted"""
    try:
        project = Projects.objects.filter(project_id=project_id)
    except Projects.DoesNotExist:
        return JsonResponse({'Error': 'Project Not Found'}, status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(project, many=True)
        return JsonResponse({'project': serializer.data})
    elif request.method == 'PUT':
        serializer = ProjectSerializer(project.first(), request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'project': serializer.data})
        return JsonResponse({'Error': 'The data is not valid'})


@api_view(['GET', 'PUT', 'DELETE'])
def employeeDetail_view(request, pk, format=None):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({'error': 'Employee does not exist 😐'}, status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response({'employee': serializer.data})
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'PUT', 'DELETE'])
def benefitslist_view(request):
    benefits = Benefits.objects.all()
    serializer = BenefitsSerializer(benefits, many=True)
    return JsonResponse(data={'benefits': serializer.data}, safe=False)
