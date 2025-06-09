from django.urls import path, include
from rest_framework import routers
from .views import PatientViewSet, DoctorViewSet, AppointmentViewSet, ChatbotResponse

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = router.urls + [
    path('chatbot/', ChatbotResponse.as_view(), name='chatbot'),
]