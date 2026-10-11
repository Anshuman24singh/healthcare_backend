
import json
import urllib.request
import urllib.error

BASE_URL = "http://127.0.0.1:8000"
ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzkxNzA3ODQwLCJpYXQiOjE3OTE3MDYwNDAsImp0aSI6IjJiMmUxOTkyYTg4ZjQ4ZmNiNjM3YzZjNmExMWMwNWFlIiwidXNlcl9pZCI6IjEifQ.ok6Jzh9m-ZwIuPDbReTmx6IDMRaAos73058_o4UN3kU"


request = urllib.request.Request(
    f"{BASE_URL}/api/patients/",
    headers={
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Accept": "application/json",
    },
    method="GET",
)

try:
    with urllib.request.urlopen(request) as response:
        print("Status:", response.status)
        data = json.loads(response.read().decode("utf-8"))
        print(json.dumps(data, indent=2))

except urllib.error.HTTPError as error:
    print("Status:", error.code)
    print(error.read().decode("utf-8"))
