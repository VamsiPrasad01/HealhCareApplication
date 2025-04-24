import requests

url = "http://127.0.0.1:8000/api/token/"
payload = {
    "username": "vamsi_a",
    "password": "Luffy@123"
}
headers = {
    "Content-Type": "application/json"
}

try:
    response = requests.post(url, json=payload, headers=headers)
    print("Status Code:", response.status_code)
    print("Response:", response.json())
except Exception as e:
    print("Error:", e)
