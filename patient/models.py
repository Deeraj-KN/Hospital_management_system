from django.db import models

class Hospital(models.Model):
    hname = models.CharField(max_length=100)
    address = models.TextField()

class Department(models.Model):
    dname = models.CharField(max_length=50)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)

class Patient(models.Model):
    STATUS_CHOICES = [
        ('primary_check', 'Primary Check'),
        ('consultation', 'Consultation'),
        ('discharged', 'Discharged'),
        ('admitted', 'Admitted'),
        ('referred', 'Referred'),
    ]

    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    disease = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    medication_remarks = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name
