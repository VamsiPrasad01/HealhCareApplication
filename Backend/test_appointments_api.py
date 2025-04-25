import requests

access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1NTQyMzA5LCJpYXQiOjE3NDU1NDIwMDksImp0aSI6IjJjYmI1YWNhZDczZTQwMmZiY2ZjZDc0NTRlN2JmNzY5IiwidXNlcl9pZCI6M30.YQkBlM8v2SYWxi6rPGxmzjP8cT8R3uCwBO_2wkEcbGU"  # Replace with new token

url = "http://127.0.0.1:8000/api/appointments/"
headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

get_response = requests.get(url, headers=headers)
print("GET Status:", get_response.status_code)
print("GET Response:", get_response.json())

payload = {
    "patient": 1,
    "doctor": 1,
    "date": "2025-04-30",          # Format: YYYY-MM-DD
    "time": "10:00:00",            # Format: HH:MM:SS
    "reason": "Routine check-up"
}


post_response = requests.post(url, headers=headers, json=payload)
print("POST Status:", post_response.status_code)
print("POST Response:", post_response.json())
