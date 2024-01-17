
from rest_framework import serializers
from .models import Hospital, Department, Patient,History

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'



class PatientSerializer1(serializers.ModelSerializer):
    
    class Meta:
        model = Patient
        fields = (
            'status', 'name'
        )
class HistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = History
        fields = '__all__'