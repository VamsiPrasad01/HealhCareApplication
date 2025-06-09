# chatbot/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny  # Use IsAuthenticated for protected access
import openai
from decouple import config

# Load OpenAI key from .env
openai.api_key = config("OPENAI_API_KEY")

class ChatbotResponse(APIView):
    permission_classes = [AllowAny]  # Or use [IsAuthenticated] if needed

    def post(self, request):
        message = request.data.get("message")
        if not message:
            return Response({"error": "Message is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Send message to OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful healthcare assistant."},
                    {"role": "user", "content": message},
                ]
            )
            reply = response.choices[0]["message"]["content"]
            return Response({"reply": reply}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
