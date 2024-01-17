
from . import views
from django.urls import path
from .views import PatientInputView,PatientInputView2,PatientInfoView,PatientInfoView_all
from .views import HomeAPIView,HospitalViews,DisplayHospitalsView,DisplayPatientsView,PatientViews,TestView

urlpatterns = [
    path('', HomeAPIView.as_view(), name='home-api'),
    path('addhospital/',HospitalViews.as_view(), name='addhospital'),

    path('addpatient/',PatientViews.as_view(), name='addpatient'),
    path('displayhospitals', DisplayHospitalsView.as_view(), name='display_hospitals'),
    path('displaypatients', DisplayPatientsView.as_view(), name='display_patients'),

    path('input/', PatientInputView.as_view(), name='patient_input'),
    path('input2/', PatientInputView2.as_view(), name='patient_input2'),

    path('patient_info/', PatientInfoView.as_view(), name='patient_info'),
    path('patient_info_all/', PatientInfoView_all.as_view(), name='patient_info_all'),
    path('test/',TestView.as_view(), name='test'),




    
]   
