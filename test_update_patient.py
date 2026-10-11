
import json
import urllib.request
import urllib.error

BASE_URL = "http://127.0.0.1:8000"
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzkxNzA3ODQwLCJpYXQiOjE3OTE3MDYwNDAsImp0aSI6IjJiMmUxOTkyYTg4ZjQ4ZmNiNjM3YzZjNmExMWMwNWFlIiwidXNlcl9pZCI6IjEifQ.ok6Jzh9m-ZwIuPDbReTmx6IDMRaAos73058_o4UN3kU"

PATIENT_ID = 1

updated_data = {
    "name": "Rahul Sharma Updated",
    "age": 29,
    "gender": "Male",
    "address": "Mumbai, Maharashtra",
    "phone_number": "9876543210",
}

request = urllib.request.Request(
    f"{BASE_URL}/api/patients/{PATIENT_ID}/",
    data=json.dumps(updated_data).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    },
    method="PUT",
)

try:
    with urllib.request.urlopen(request) as response:
        print("Status:", response.status)
        print(response.read().decode("utf-8"))

except urllib.error.HTTPError as error:
    print("Status:", error.code)
    print(error.read().decode("utf-8"))
