from django.urls import path
from .views import VisitListView1
from .views import VisitListView2

urlpatterns = [
    path('status/<str:patient_name>/', VisitListView1.as_view(), name='visit-list'),
    path('allvisits/<str:patient_name>/', VisitListView2.as_view(), name='visit-list'),
]