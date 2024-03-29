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
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'Success': "Login Successful"})
        return JsonResponse({"Error": 'Try creating an account first'})


@api_view(['GET', 'POST'])
@login_required
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
@login_required
def projectList_view(request):
    if request.method == 'GET':
        projects = Projects.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return JsonResponse({'projects': serializer.data})
    serializer = ProjectSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'project': serializer.data})


@api_view(['GET', 'PUT', 'DELETE'])
@login_required
def projectDetail_view(request, project_id):
    """ Use project id to get the details of the project. If by any chance two projects have the same project id(
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
    elif request.method == 'DELETE':
        project.delete()
        return JsonResponse({'Success': 'Project Not found'})


@api_view(['GET', 'PUT', 'DELETE'])
@login_required
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


@api_view(['GET', 'POST'])
@login_required
def benefitslist_view(request):
    if request.method == 'GET':
        benefits = Benefits.objects.all()
        serializer = BenefitsSerializer(benefits, many=True)
        return JsonResponse(data={'benefits': serializer.data}, safe=False)
    serializer = BenefitsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({'benefits': serializer.data})


@api_view(['GET', 'PUT', 'DELETE'])
@login_required
def benefitdetail_view(request, pk):
    try:
        benefit = Benefits.objects.filter(pk=pk)
    except Benefits.DoesNotExist:
        return JsonResponse({"Error": "No User or Benefits with that ID"})

    if request.method == 'GET':
        serializer = BenefitsSerializer(benefit, many=True)
        return JsonResponse({'Benefit': serializer.data})
    elif request.method == 'PUT':
        serializer = BenefitsSerializer(benefit.first(), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'Benefit': serializer.data})
        return JsonResponse({'Error': 'Invalid Input'})
    elif request.method == 'DELETE':
        benefit.delete()
        return JsonResponse({'Success': 'Benefit has been deleted'})


def createUser(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        first_name = request.POST.get('name')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))
        user = User(username=username, first_name=first_name, email=email, password=password)
        if user:
            user.save()
            return JsonResponse({'Success': 'User created successfully!'})
        return JsonResponse({'Error', 'Check your details and try changing your username'})
