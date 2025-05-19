from rest_framework import viewsets
from .models import Patient, Doctor, Appointment
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import openai

class HealthAssistantView(APIView):
    def post(self, request):
        question = request.data.get("question")
        if not question:
            return Response({"error": "No question provided"}, status=400)

        openai.api_key = settings.OPENAI_API_KEY

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": question}],
            )
            answer = response.choices[0].message["content"]
            return Response({"answer": answer})
        except Exception as e:
            return Response({"error": str(e)}, status=500)
