
import urllib.request
import urllib.error

BASE_URL = "http://127.0.0.1:8000"
ACCESS_TOKEN = input("Paste your current JWT access token: ").strip()
PATIENT_ID = 1

request = urllib.request.Request(
    f"{BASE_URL}/api/patients/{PATIENT_ID}/",
    headers={
        "Authorization": f"Bearer {ACCESS_TOKEN}",
    },
    method="DELETE",
)

try:
    with urllib.request.urlopen(request) as response:
        print("Status:", response.status)
        print("Patient deleted successfully.")

except urllib.error.HTTPError as error:
    print("Status:", error.code)
    print(error.read().decode("utf-8"))
