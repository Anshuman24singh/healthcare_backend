
import json
import urllib.request
import urllib.error

BASE_URL = "http://127.0.0.1:8000"
ACCESS_TOKEN = input("Paste your current JWT access token: ").strip().strip('"').strip("'")

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
