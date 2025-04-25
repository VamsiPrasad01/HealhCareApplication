import requests

access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1NTQxOTAyLCJpYXQiOjE3NDU1NDE2MDIsImp0aSI6IjU1ZDdlYTc2MGY1OTQ1ZTc5Yjg1OTNlZGI1OGYwM2JkIiwidXNlcl9pZCI6M30.x724MSReYROD0pN4Kb2InkH8yhBP0VRp7lw0Y844wUI"  # Replace with fresh token

# 1️⃣ Test GET
get_url = "http://127.0.0.1:8000/api/doctors/"
headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

get_response = requests.get(get_url, headers=headers)
print("GET Status Code:", get_response.status_code)
print("GET Response:", get_response.json())

# 2️⃣ Test POST
post_payload = {
    "name": "Dr. Jane Smith",
    "specialty": "Cardiology",
    "email": "dr.jane@example.com"
}

post_response = requests.post(get_url, headers=headers, json=post_payload)
print("POST Status Code:", post_response.status_code)
print("POST Response:", post_response.json())
