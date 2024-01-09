# hospital_management_app/urls.py
from . import views
from django.urls import path
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import DepartmentManagementView, PatientManagementView, PatientStatusUpdateView, PatientInfoRetrievalView
from .views import VisitListView1
from .views import VisitListView2,AddHospitalAPIView,AddPatientAPIView
from .views import PatientInputView,PatientInputView2,PatientInfoView,PatientInfoView_all,create_patient,list_patient
urlpatterns = [
    path('', views.home, name='home'),
    path('addhospital',views.addhospital, name='addhospital'),
    path('addpatient',views.addpatient, name='addpatient'),
    path('displayhospitals',views.displayhospitals, name='displayhospitals'),
    path('displaypatients',views.displaypatients, name='displaypatients'),



    #api views 
    path('addhospital2',AddHospitalAPIView.as_view(), name='addhospital2'),
    path('addpatient2',AddPatientAPIView.as_view(), name='addpatient2'),

    path('input/', PatientInputView.as_view(), name='patient_input'),
    path('input2/', PatientInputView2.as_view(), name='patient_input2'),
    path('status/<str:patient_name>/', VisitListView1.as_view(), name='visit-list'),
    path('patient_info/', PatientInfoView.as_view(), name='patient_info'),
    path('allvisits/<str:patient_name>/', VisitListView2.as_view(), name='visit-list1'),
    path('patient_info_all/', PatientInfoView_all.as_view(), name='patient_info_all'),


    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('patient/create/',create_patient,name='create_patient'),
    path('patients/',list_patient,name='list_patient')
]   
