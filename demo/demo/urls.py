"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from employees.views import employeesDetailView
#from employees.views import employeesDetailView
from employees.views import addEmployees
from employees.views import deleteEmployees


from home.views import addDepartment
from employees.views import searchemployees, employeesListview, editEmployees
from home.models import department

from employees import views as employees
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from accounts.views import SignUpView
from home.views import SearchResultsView
from home.views import departmentListView
from home.views import deleteDepartment, successView


urlpatterns = [
    # account path
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('signup/', SignUpView.as_view(), name="signup"),
    # department path
    path('', departmentListView.as_view(), name="home"),
    path('addDepartmentForm/',
         addDepartment.as_view(model=department, success_url="/")),
    path('delete/<int:pk>/', deleteDepartment.as_view()),
    path("search/", SearchResultsView.as_view(), name="search_results"),
    # employees path

    #path('addEmployeesForm/', employees.get_employees_form),
    path('addEmployees/', addEmployees.as_view()),
    path('editEmployees/<int:pk>/', editEmployees.as_view()),
    #path('updateemployees/<int:id>', employees.update_employees),
    path("searchemployees/", searchemployees.as_view(), name="searchemployees"),
    path('department/<int:pk>', employeesDetailView.as_view(), name="listemployees"),
    #path('department/<int:id>/', employees.get_employees, name="listemployees"),
    path('deleteEmployees/<int:pk>/', deleteEmployees.as_view(), name='delete_em'),
    path('employeesListview/', employeesListview.as_view()),
    path('addEmployees/success/', successView.as_view()),
    path('deleteEmployees/<int:id>/success', successView.as_view()),
    path('editEmployees/<int:id>/success', successView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Qhieu19"
