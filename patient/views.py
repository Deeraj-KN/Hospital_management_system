# hospital_management_app/views.py
from datetime import datetime
from django.shortcuts import redirect, render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Hospital, Department, Patient,History
from rest_framework import generics,status
from .serialzers import HospitalSerializer, DepartmentSerializer, PatientSerializer
from .serialzers import PatientSerializer1,PatientSerializer2
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from django.contrib.auth.decorators import login_required



@login_required(login_url='signin')
def home(request):
    return render(request,'home.html')


class HomeApiView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        return Response(status=status.HTTP_200_OK)

################################ using fun
@login_required(login_url='signin')
def addhospital(request):
    departments=Department.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        address = request.POST['address']
        department_ids = request.POST.getlist('department')  # Use getlist to handle multiple selections
        hospital=Hospital.objects.create(hname=name, address=address)
        hospital.department.set(department_ids)
        return redirect('/patient')
    return render(request,'addhospital.html',{'departments':departments})

################################ converted to api format

class AddHospitalAPIView(APIView):
    def post(self, request,*args,**kwargs):
        serializer=HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST, body=request)
#################################adding patient function
@login_required(login_url='signin')
def addpatient(request):
    hospitals = Hospital.objects.all()

    if request.method == 'POST':

        name = request.POST['name']
        hospital_id = request.POST['hospital']
        #disease = request.POST['disease']
        doctor_name = request.POST['doctor_name']
        status = request.POST['status']
        dob = request.POST['dob']
        ph_number = request.POST['ph_number']
        hospital = Hospital.objects.get(pk=hospital_id)
        existing_patient=Patient.objects.filter(ph_number=ph_number).first()
        if existing_patient:
            #patient=Patient.objects.get(name=name)
            existing_patient.hospital=hospital
            existing_patient.doctor_name=doctor_name
            existing_patient.status=status
            existing_patient.dob=dob
            existing_patient.ph_number=ph_number
            existing_patient.save()
            History.objects.create(patient=existing_patient,hospital=hospital,date=datetime.now())
            

        
        else:
            # Create and save the Patient object
            patient = Patient.objects.create(
                name=name,
                hospital=hospital,
                doctor_name=doctor_name,
                status=status,
                dob=dob,
                ph_number=ph_number,
            )
            History.objects.create(patient=patient,hospital=hospital,date=datetime.now())

        # Redirect to the home page or any other desired page after submission
        return redirect('/patient')

    return render(request,'addpatient.html',{'hospitals':hospitals})

################################ converted to api format

class AddPatientAPIView(APIView):
    def post(self, request,*args,**kwargs):
        serializer=PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST, body=request)
    



@login_required(login_url='signin')
def displayhospitals(request):
    hospitals=Hospital.objects.all()
    return render(request,'displayhospitals.html',{'hospitals':hospitals})

@login_required(login_url='signin')
def displaypatients(request):
    patients=Patient.objects.all()
    return render(request,'displaypatients.html',{'patients':patients})


class DepartmentManagementView(APIView):
    def get(self, request, hospital_id):
        hospital = get_object_or_404(Hospital, pk=hospital_id)
        departments = hospital.department_set.all()
        return render(request, 'department_management.html', {'hospital': hospital, 'departments': departments})

    def post(self, request, hospital_id):
        # Handle department creation
        # ...
        pass

class PatientManagementView(APIView):
    def get(self, request):
        hospitals = Hospital.objects.all()
        return render(request, 'patient_management.html', {'hospitals': hospitals})

    def post(self, request):
        # Handle patient creation
        # ...
        pass

class PatientStatusUpdateView(APIView):
    def get(self, request, patient_id):
        patient = get_object_or_404(Patient, pk=patient_id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def post(self, request, patient_id):
        # Handle patient status update

        # ...
        pass

class PatientInfoRetrievalView(APIView):
    def get(self, request, patient_name):
        patients = Patient.objects.filter(name=patient_name)
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)






class VisitListView1(generics.ListAPIView):
    serializer_class = PatientSerializer1
    def get_queryset(self):
        patient_name = self.kwargs.get('patient_name')
        # if we want to access from postman params patient_name = self.request.data.get('patient_name')
        patient_name = Patient.objects.get(name=patient_name)
        last_patient=Patient.objects.filter(name=patient_name).last()
        return Patient.objects.filter(patient_id=last_patient.patient_id) if last_patient else Patient.objects.none()
    def get(self, request, *args, **kwargs):
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            patient_data = serializer.data[0] if serializer.data else {}

            return render(request, 'patient_info.html', {'patient': patient_data})


class VisitListView2(generics.ListAPIView):
    serializer_class = PatientSerializer2
    def get_queryset(self):
        patient_name = self.kwargs.get('patient_name')
        # if we want to access from postman params patient_name = self.request.data.get('patient_name')
        # patient = Patient.objects.get(name=patient_name)
        return Patient.objects.filter(name=patient_name)
    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        patients_data = serializer.data

        return render(request, 'patient_info_all.html', {'patients': patients_data})
    


# @login_required(login_url='signin')
# class VisitListView1(generics.ListAPIView):
#     serializer_class = PatientSerializer1
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'patient_info.html'

#     def get_queryset(self):
#         patient_name = self.kwargs.get('patient_name')
#         last_patient = Patient.objects.filter(name=patient_name).last()
#         return Patient.objects.filter(patient_id=last_patient.patient_id) if last_patient else Patient.objects.none()

#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         patient_data = serializer.data[0] if serializer.data else {}

#         # Check if the request is AJAX
#         if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
#             return JsonResponse(patient_data)
#         else:
#             return Response({'patient': patient_data})
        
# @login_required(login_url='signin')
# class VisitListView2(generics.ListAPIView):
#     serializer_class = PatientSerializer2
#     renderer_classes = [TemplateHTMLRenderer]
#     template_name = 'patient_info_all.html'

#     def get_queryset(self):
#         patient_name = self.kwargs.get('patient_name')
#         return Patient.objects.filter(name=patient_name)

#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         patients_data = serializer.data

#         # Check if the request is AJAX
#         if request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
#             return JsonResponse(patients_data, safe=False)
#         else:
#             return Response({'patients': patients_data})

class PatientInputView(View):
    def get(self, request):
        return render(request, 'input_form.html')
    
class PatientInputView2(View):
    def get(self, request):
        return render(request, 'input_form2.html')

class PatientInfoView(View):
    def post(self, request, *args, **kwargs):
        # Get the patient name from the form submission
        patient_name = request.POST.get('name')

        # Redirect to the VisitListView1 with the extracted patient name
        return redirect('visit-list', patient_name=patient_name)
    
class PatientInfoView_all(View):
    def post(self, request, *args, **kwargs):
        # Get the patient name from the form submission
        patient_name = request.POST.get('name')

        # Redirect to the VisitListView2 with the extracted patient name
        return redirect('visit-list1', patient_name=patient_name)



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
    serializer=PatientSerializer(patients,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)