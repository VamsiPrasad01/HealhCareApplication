from django.urls import path
from .views import ChatbotResponse

urlpatterns = [
    path('', ChatbotResponse.as_view(), name='chatbot'),
]
