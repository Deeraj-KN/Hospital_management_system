from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = (
            'status', 'name'
        )
class PatientSerializer2(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = (
            'date','status', 'name','doctor_name',
        )