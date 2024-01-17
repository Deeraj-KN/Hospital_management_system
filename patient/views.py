from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hospital, Department, Patient,History
from rest_framework import generics,status
from .serialzers import HospitalSerializer, DepartmentSerializer, PatientSerializer
from .serialzers import PatientSerializer1,HistorySerializer
from django.views import View
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from .forms import HospitalForm,PatientForm,DepartmentForm



class HomeAPIView(APIView):
    def get(self, request):
        return render(request, 'home.html')

class PatientViews(APIView):
    template_name = 'addpatient.html'

    def get(self, request, *args, **kwargs):
        hospitals = Hospital.objects.all()
        return render(request, self.template_name, {'hospitals': hospitals})

    def post(self, request, *args, **kwargs):
        form = PatientForm(request.POST)
        if form.is_valid():
            ph_number = form.cleaned_data['ph_number']
            name=form.cleaned_data['name']
            # Check if the patient with the given phone number already exists
            try:
                existing_patient = Patient.objects.get(name=name,ph_number=ph_number)
                
                if existing_patient:
                    # Update the existing patient's information
                    existing_patient.hospital = form.cleaned_data['hospital']
                    existing_patient.doctor_name = form.cleaned_data['doctor_name']
                    existing_patient.status = form.cleaned_data['status']
                    existing_patient.dob = form.cleaned_data['dob']
                    existing_patient.save()

                    # Create a history entry for the existing patient
                    History.objects.create(
                        patient=existing_patient,
                        hospital=form.cleaned_data['hospital'],
                        date=datetime.now(),
                        ph_number=ph_number
                    )
                    
            except Patient.DoesNotExist:
                patient = form.save()
                History.objects.create(
                        patient=patient,
                        hospital=patient.hospital,
                        date=datetime.now(),
                        ph_number=ph_number
                    )
            return redirect('/patient')

        else:
            # Handle form validation errors
            print(form.errors)
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
        

class HospitalViews(APIView):
    template_name = 'addhospital.html'

    def get(self, request, *args, **kwargs):
        departments = Department.objects.all()
        return render(request, self.template_name, {'departments': departments})

    def post(self, request, *args, **kwargs):
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/patient')  
        else:
            print(form.errors)
        

class DisplayHospitalsView(APIView):
    template_name = 'displayhospitals.html'

    def get(self, request, *args, **kwargs):
        hospitals = Hospital.objects.all()
        return render(request, self.template_name, {'hospitals': hospitals})

class DisplayPatientsView(APIView):
    template_name = 'displaypatients.html'

    def get(self, request, *args, **kwargs):
        patients = Patient.objects.all()
        return render(request, self.template_name, {'patients': patients})


class PatientInputView(APIView):
    def get(self, request):
        return render(request, 'input_form.html')
    
class PatientInputView2(APIView):
    def get(self, request):
        return render(request, 'input_form2.html')

class PatientInfoView(APIView):
    serializer_class = PatientSerializer1
    def post(self, request, *args, **kwargs):
        # Get the patient name from the form submission
        patient_name = request.POST.get('name')
        ph_number = request.POST.get('ph_number')
        try:
            patients=Patient.objects.filter(name=patient_name,ph_number=ph_number)
            patient_data=None
            if patients.exists():
                last_patient=patients.last()
                serializer=PatientSerializer1(last_patient, data=last_patient.__dict__)
                if serializer.is_valid():
                    patient_data = serializer.data
            return render(request, 'patient_info.html', {'patient': patient_data})
        
        except Patient.DoesNotExist:
            return Response({'error':'patient not found'},status=404)


class PatientInfoView_all(APIView):
    def post(self, request, *args, **kwargs):
        patient_name = request.POST.get('name')
        ph_number = request.POST.get('ph_number')
        patient = Patient.objects.get(name=patient_name, ph_number=ph_number)
        
        if patient:
            # Query the history for the patient
            patients_history = History.objects.filter(patient=patient)
            patient_data = None

            if patients_history.exists():
                serializer = HistorySerializer(patients_history, many=True, context={'request': request})
                patient_data = serializer.data

            return render(request, 'patient_info_all.html', {'patients': patient_data, 'patient_name': patient_name})

#for learning purposes only using postman
@api_view(['POST'])
def create_patient(request):
    serializer=PatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def list_patient(request):
    patients=Patient.objects.all()
    serializer=PatientSerializer(data=patients,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


#learning purpose 
class TestView(APIView):
    def get(self, request):
        patients=Patient.objects.all()
        serializer=PatientSerializer(patients,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self, request,args,**kwargs):
        serializer=PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)