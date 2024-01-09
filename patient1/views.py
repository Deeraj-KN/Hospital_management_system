from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import PatientSerializer,PatientSerializer2
from .models import Patient

class VisitListView1(generics.ListAPIView):
    serializer_class = PatientSerializer
    def get_queryset(self):
        patient_name = self.kwargs.get('patient_name')
        # if we want to access from postman params patient_name = self.request.data.get('patient_name')
        #patient = Patient.objects.get(name=patient_name)
        last_patient=Patient.objects.filter(name=patient_name).last()
        return Patient.objects.filter(id=last_patient.id) if last_patient else Patient.objects.none()
class VisitListView2(generics.ListAPIView):
    serializer_class = PatientSerializer2
    def get_queryset(self):
        patient_name = self.kwargs.get('patient_name')
        # if we want to access from postman params patient_name = self.request.data.get('patient_name')
        # patient = Patient.objects.get(name=patient_name)
        return Patient.objects.filter(name=patient_name)