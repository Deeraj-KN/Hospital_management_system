
from django import forms
from .models import Hospital, Department,Patient

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields='__all__'