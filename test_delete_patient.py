
import json
import urllib.request
import urllib.error

BASE_URL = "http://127.0.0.1:8000"
ACCESS_TOKEN = input("Paste your current JWT access token: ").strip().strip('"').strip("'")

def api_request(path, method="GET", data=None):
    body = json.dumps(data).encode("utf-8") if data is not None else None

    request = urllib.request.Request(
        f"{BASE_URL}{path}",
        data=body,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json",
        },
        method=method,
    )

    try:
        with urllib.request.urlopen(request) as response:
            content = response.read().decode("utf-8")
            return response.status, content
    except urllib.error.HTTPError as error:
        return error.code, error.read().decode("utf-8")

# Create a patient owned by the logged-in user
status, response = api_request(
    "/api/patients/",
    "POST",
    {
        "name": "Delete Test Patient",
        "age": 30,
        "gender": "Male",
        "address": "Test Address",
        "phone_number": "9876543210",
    },
)

print("Create patient:", status, response)

if status != 201:
    print("Could not create patient. Check the response above.")
    raise SystemExit(1)

patient = json.loads(response)
patient_id = patient["id"]

# Delete the patient we just created
status, response = api_request(f"/api/patients/{patient_id}/", "DELETE")
print("Delete patient:", status)

if status == 204:
    print("PASS: Patient created and deleted successfully.")
else:
    print(response)
