from django.db import models
from django.utils import timezone
class Department(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    dname = models.CharField(max_length=50)  # Change 'name' to 'dname'


class Hospital(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    hname = models.CharField(max_length=100)
    address = models.TextField()
    department=models.ManyToManyField(Department)





class Patient(models.Model):
    STATUS_CHOICES = [
        ('primary_check', 'Primary Check'),
        ('consultation', 'Consultation'),
        ('discharged', 'Discharged'),
        ('admitted', 'Admitted'),
        ('referred', 'Referred'),
    ]

    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    #disease = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    #medication_remarks = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    ph_number = models.CharField(max_length=15, blank=True,default="")
    dob = models.DateField(default=timezone.now, blank=False, null=False)
    def __str__(self):
        return self.name
class History(models.Model):
    id=models.AutoField(primary_key=True)
    patient=models.ForeignKey('Patient',on_delete=models.DO_NOTHING)
    date=models.DateTimeField()
    hospital=models.ForeignKey('Hospital', on_delete=models.DO_NOTHING)
