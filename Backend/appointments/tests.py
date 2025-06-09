from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Patient, Doctor, Appointment
from datetime import date, time

class AppointmentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.patient = Patient.objects.create(name='John Doe', email='john@example.com', phone='1234567890')
        self.doctor = Doctor.objects.create(name='Dr. Smith', specialty='Cardiology', email='smith@example.com')
        self.appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            date=date(2025, 6, 10),
            time=time(10, 0),
            status='Booked'
        )

    def test_create_patient(self):
        response = self.client.post('/api/appointments/patients/', {
            'name': 'Jane Doe',
            'email': 'jane@example.com',
            'phone': '0987654321'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Patient.objects.count(), 2)

    def test_get_appointments(self):
        response = self.client.get('/api/appointments/appointments/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['patient'], 'John Doe')

    def test_delete_appointment(self):
        response = self.client.delete(f'/api/appointments/appointments/{self.appointment.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Appointment.objects.count(), 0)