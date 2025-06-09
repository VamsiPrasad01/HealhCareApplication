from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import ChatMessage
import requests_mock

class ChatbotTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_chatbot_response(self):
        with requests_mock.Mocker() as m:
            m.post(
                'https://api.x.ai/v1/chat/completions',
                json={
                    'choices': [{'message': {'content': 'Test reply'}}]
                },
                status_code=200
            )
            response = self.client.post('/api/chatbot/', {'message': 'Hello'})
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data['reply'], 'Test reply')
            self.assertEqual(ChatMessage.objects.count(), 1)
            chat = ChatMessage.objects.first()
            self.assertEqual(chat.message, 'Hello')
            self.assertEqual(chat.response, 'Test reply')

    def test_chatbot_empty_message(self):
        response = self.client.post('/api/chatbot/', {'message': ''})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['error'], 'Message is required')