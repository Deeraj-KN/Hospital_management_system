from django.db import models

# Create your models here.
from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    remarks = models.TextField()
    date = models.DateField(auto_now_add=True)