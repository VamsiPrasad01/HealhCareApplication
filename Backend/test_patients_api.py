import requests

url = "http://127.0.0.1:8000/api/patients/"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1NTQxNDUzLCJpYXQiOjE3NDU1NDExNTMsImp0aSI6ImQ5MTJkNmQzZjdhMjQ1NzNiMDQ4NWY3YTBkNmQ4MDZhIiwidXNlcl9pZCI6M30.BLFFYly8ypxv7lH9eVoZtWsQd_ahMdMBNCIKveqTDP8",
    "Content-Type": "application/json"
}

print("Sending request...")
response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

try:
    print("Response:", response.json())
except Exception as e:
    print("Failed to decode JSON:", e)
    print("Raw response:", response.text)
