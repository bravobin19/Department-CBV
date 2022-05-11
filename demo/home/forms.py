from django import forms
from .models import department as department_model


class departmentForm(forms.ModelForm):
    class Meta:

        model = department_model

        fields = [
            "name"
        ]
