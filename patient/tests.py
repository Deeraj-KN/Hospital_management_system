from django.test import TestCase
from django.utils import timezone
from .models import Department, Hospital, Patient, History

class ModelsTestCase(TestCase):
    def setUp(self):
        # Create a department
        self.department = Department.objects.create(dname='Neurology')

        # Create a hospital
        self.hospital = Hospital.objects.create(hname='G Hospital', address='123 Main St')
        self.hospital.department.add(self.department)

        # Create a patient
        self.patient = Patient.objects.create(
            name='Shuchith',
            hospital=self.hospital,
            doctor_name='Dr.',
            status='primary_check',
            ph_number='8974563210',
            dob='2002-01-01',
        )

        # Create a history entry
        self.history_entry = History.objects.create(
            patient=self.patient,
            date=timezone.now(),
            hospital=self.hospital
        )

    def test_department_model(self):
        department = Department.objects.get(dname='Neurology')
        self.assertEqual(department.dname, 'Neurology')

    def test_hospital_model(self):
        hospital = Hospital.objects.get(hname='G Hospital')
        self.assertEqual(hospital.address, '123 Main St')
        self.assertEqual(hospital.department.count(), 1)
        self.assertEqual(hospital.department.first().dname, 'Neurology')

    def test_patient_model(self):
        patient = Patient.objects.get(name='Shuchith')
        self.assertEqual(patient.hospital, self.hospital)
        self.assertEqual(patient.status, 'primary_check')
        self.assertEqual(patient.history_set.count(), 1)

    def test_history_model(self):
        history_entry = History.objects.get(patient=self.patient)
        self.assertEqual(history_entry.hospital, self.hospital)
        self.assertEqual(history_entry.date.date(), timezone.now().date())





