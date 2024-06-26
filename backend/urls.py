"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import employeeList_view
from .views import projectList_view
from .views import employeeDetail_view
from .views import benefitslist_view
from .views import projectDetail_view
from .views import benefitdetail_view
from .views import home_view
from .views import createUser
from .views import login_view
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('employees/', employeeList_view),
    path('projects/', projectList_view),
    path('employees/<int:pk>/', employeeDetail_view),
    path('benefits/', benefitslist_view),
    path('project/<int:project_id>', projectDetail_view),
    path('benefit/<int:pk>', benefitdetail_view),
    path('create/', createUser),
    path('login/', login_view),
]


urlpatterns = format_suffix_patterns(urlpatterns)