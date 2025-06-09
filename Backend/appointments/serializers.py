from rest_framework import serializers
from .models import Patient, Doctor, Appointment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    patient = serializers.CharField(source='patient.name', read_only=True)
    doctor = serializers.CharField(source='doctor.name', read_only=True)

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'date', 'time', 'notes', 'status']