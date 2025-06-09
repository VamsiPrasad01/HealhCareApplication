from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Patient, Doctor, Appointment
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer
import requests
from decouple import config
from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class ChatbotResponse(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message = request.data.get("message")
        if not message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        if len(message) > 1000:
            return Response({"error": "Message too long"}, status=status.HTTP_400_BAD_REQUEST)

        cache_key = f"chatbot_response_{hash(message)}"
        cached_response = cache.get(cache_key)
        if cached_response:
            return Response({"reply": cached_response, "cached": True})

        try:
            response = requests.post(
                'https://api.x.ai/v1/chat/completions',
                headers={
                    'Authorization': f'Bearer {config("XAI_API_KEY")}',
                    'Content-Type': 'application/json',
                },
                json={
                    'model': 'grok-3',
                    'messages': [
                        {
                            'role': 'system',
                            'content': (
                                'You are Grok, a healthcare assistant created by xAI. '
                                'Provide general information and clarify that you are not a doctor. '
                                'Encourage users to consult a healthcare professional for medical advice.'
                            ),
                        },
                        {'role': 'user', 'content': message},
                    ],
                    'max_tokens': 500,
                    'temperature': 0.7,
                },
                timeout=10
            )
            response.raise_for_status()
            reply = response.json()['choices'][0]['message']['content']
            cache.set(cache_key, reply, timeout=3600)
            return Response({
                'reply': reply,
                'disclaimer': 'This is not medical advice. Consult a healthcare professional.'
            })
        except requests.exceptions.HTTPError as e:
            return Response({"error": f"xAI API error: {str(e)}"}, status=status.HTTP_502_BAD_GATEWAY)
        except requests.exceptions.RequestException as e:
            return Response({"error": f"Unexpected error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)