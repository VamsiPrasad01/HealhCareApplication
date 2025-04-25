import requests

url = "http://127.0.0.1:8000/api/patients/"
headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1NTQxNjU2LCJpYXQiOjE3NDU1NDEzNTYsImp0aSI6ImM5MDY3YWQ0OTU5NTRhMGM4N2JiMjBiYjcxNWU1MzgyIiwidXNlcl9pZCI6M30.7s26_i4RJtH6abVCBGDsplqFbX9_91DPlN9498oNVxA",  # Replace this with fresh token
    "Content-Type": "application/json"
}

payload = {
    "name": "John Joe",
    "email": "john.Joe@example.com",
    "phone": "1234567890"
}

response = requests.post(url, headers=headers, json=payload)

print("Status Code:", response.status_code)
print("Response:", response.json())
