from django import forms
from .models import employees as employees_model


class employeesForm(forms.ModelForm):
    class Meta:

        model = employees_model

        fields = [
            "department_id"
            "name",
            "age",
            "avatar",
            "cv"
        ]
