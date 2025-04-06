from django.urls import include, path
from rest_framework import routers
from .views import PatientViewSet, DoctorViewSet, AppointmentViewSet

router = routers.DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
