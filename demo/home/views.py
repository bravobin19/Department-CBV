from django.forms import ValidationError
from lib2to3.fixes.fix_input import context

from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView

from .models import department as department_model
from employees.models import employees
from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView

# Create your views here.


class departmentListView(ListView):
    model = department_model
    template_name = 'home.html'
    context_object_name = 'department_list'


class SearchResultsView(ListView):
    model = department_model
    template_name = 'search_results.html'

    def get_queryset(self):
        context = {
            'error': 0,
            'msg': ''
        }
        query = self.request.GET.get("q")
        if not query:
            context['error'] = 1
            context['msg'] = 'Name not valid'
            raise ValidationError
        if not context['error']:
            query = self.request.GET.get("q")
            object_list = department_model.objects.filter(
                Q(name__icontains=query) | Q(
                    department_id__icontains=query)
            )
        return object_list


class addDepartment(CreateView):

    model = department_model

    fields = ['name']

    template_name = 'department_form.html'


class deleteDepartment(DeleteView):

    model = department_model

    success_url = "/"

    template_name = 'delete.html'


class successView(TemplateView):
    template_name = "em.html"