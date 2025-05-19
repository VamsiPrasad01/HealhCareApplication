
import requests

url = "http://127.0.0.1:8000/api/ask/"
question = {
    "question": "What are common symptoms of diabetes?"
}

response = requests.post(url, json=question)

if response.status_code == 200:
    print("AI Response:", response.json()["answer"])
else:
    print("Error:", response.status_code, response.text)
