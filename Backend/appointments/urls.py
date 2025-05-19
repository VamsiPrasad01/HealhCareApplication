from django.urls import path, include
from .views import HealthAssistantView
from rest_framework import routers
from .views import PatientViewSet, DoctorViewSet, AppointmentViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = router.urls + [
    path('health-assistant/', HealthAssistantView.as_view(), name='health-assistant'),
]