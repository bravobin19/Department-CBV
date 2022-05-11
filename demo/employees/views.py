
from email import message
import genericpath
from re import template
from sre_constants import SUCCESS

from turtle import update
from typing import Generic
from django import forms
from django.shortcuts import render, redirect
from datetime import datetime
from dateutil import parser
from django.urls import reverse_lazy
from home.models import department

from home.views import departmentListView
from .models import employees as employees_model
from home.models import department as department_model
from .models import employees
from django.views.generic import DetailView, ListView, UpdateView
from django.db.models import Q
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView


# def get_employees(request, id):

#     employees_list = employees_model.objects.filter(department_id=id)
#     department = department_model.objects.get(department_id=id)
#     return render(request, 'employees.html', {'employees_list': employees_list, 'department': department})


'''
def get_employees_form(request):
    department_list = department_model.objects.filter()
    return render(request, 'employees_form.html', {'department_list': department_list})
'''
'''
def add_employees(request):
    context = {
        'error': 0,
        'msg': ''
    }

    if request.method == 'POST':

        department_id = request.POST['department']

        name = request.POST['fullName']
        age = request.POST['age']
        avatar = request.FILES['avatar']
        cv = request.FILES['cv']

        # Check valid name
        # Check length <=255
        if not name:
            context['error'] = 1
            context['msg'] = 'Name not valid'
        # Check Valid age
        if age:
            try:
                age_datetime = parser.parser(age)
            except:
                context['error'] = 1
                context['msg'] = 'Age not valid'
        else:
            context['error'] = 1
            context['msg'] = 'Age not valid'
        #

        #
        if not context['error']:
            department = department_model.objects.get(
                department_id=department_id)

            employees = employees_model.objects.create(
                department_id=department,
                name=name,
                avatar=avatar,
                age=age,
                cv=cv,
            )
            employees.save()
            return redirect('/department/'+str(department_id))

    return render(request, 'error.html', context=context)
'''

'''
def edit_employees(request, id):
    editemployees = employees_model.objects.get(employees_id=id)
    return render(request, "editemployees.html", {"employees": editemployees})
'''

'''
def update_employees(request, id):

    avatar = request.FILES.get('avatar')
    cv = request.FILES.get('cv')

    employees = employees_model.objects.get(employees_id=id)

    if avatar:
        employees.avatar = avatar

    if cv:
        employees.cv = cv

    employees.save()
    return render(request, "editemployees.html", )
'''

class editEmployees(UpdateView):
    model = employees_model

    fields = ['department_id', 'name', 'age', 'avatar', 'cv'

              ]

    template_name = 'editemployees.html'

    success_url = "success"


class deleteEmployees(DeleteView):

    model = employees_model
    template_name = 'delete.html'

    success_url = "success"


class searchemployees(ListView):
    model = employees
    template_name = 'searchemployees.html'

    def get_queryset(self):
        context = {
            'error': 0,
            'msg': ''
        }

        query = self.request.GET.get("q")
        if not query:
            context['error'] = 1
            context['msg'] = 'Name not valid'
        if not context['error']:
            query = self.request.GET.get("q")
            object_list = employees.objects.filter(
                Q(name__icontains=query) | Q(
                    employees_id__icontains=query)
            )
        return object_list


class addEmployees(CreateView):

    model = employees_model

    fields = ['department_id', 'name', 'age', 'avatar', 'cv']

    template_name = 'employees_form.html'
    success_url = "success/"


''''
class departmentForm(forms.ModelForm):
    class Meta:

        model = department_model

        fields = [
            "name"
        ]
'''


class employeesDetailView(DetailView):
    model = department_model

    template_name = "employees.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['employees_list'] = employees_model.objects.all()
        return context


class employeesListview(ListView):
    model = department_model

    template_name = "em.html"

    context_object_name = 'employees_list'


