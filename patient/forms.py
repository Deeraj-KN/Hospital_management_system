
from django import forms
from .models import Hospital, Department

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name', 'address']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name']
