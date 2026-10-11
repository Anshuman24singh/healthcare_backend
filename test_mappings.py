
import json
import urllib.request
import urllib.error

BASE_URL = "http://127.0.0.1:8000"
ACCESS_TOKEN ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzkxNzE3OTU0LCJpYXQiOjE3OTE3MTYxNTQsImp0aSI6Ijg0MjRmMDJiMWI5MzQwY2FiYWZiZjgzYzYxMGU3YmVkIiwidXNlcl9pZCI6IjEifQ.m_ANmfXYi_4L3xvPCuLWht8sl-oIVgXOJFQ_88l5dJ0"



def send_request(path, method="GET", data=None):
    body = None if data is None else json.dumps(data).encode("utf-8")

    request = urllib.request.Request(
        f"{BASE_URL}{path}",
        data=body,
        headers={
            "Authorization": f"Bearer {ACCESS_TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method=method,
    )

    try:
        with urllib.request.urlopen(request) as response:
            result = response.read().decode("utf-8")
            print(f"\n{method} {path}")
            print("Status:", response.status)
            print(result or "Request successful")
            return json.loads(result) if result else None

    except urllib.error.HTTPError as error:
        print(f"\n{method} {path}")
        print("Status:", error.code)
        print(error.read().decode("utf-8"))
        return None


# First create a new patient because the earlier test patient was deleted.
patient_data = {
    "name": "Rahul Sharma",
    "age": 29,
    "gender": "Male",
    "address": "Mumbai, Maharashtra",
    "phone_number": "9876543210",
}

patient = send_request("/api/patients/", "POST", patient_data)

if patient:
    patient_id = patient["id"]

    # Create a doctor if one with this email doesn't already exist.
    doctor_data = {
        "name": "Dr. Priya Sharma",
        "specialization": "Cardiology",
        "email": "priya.sharma@example.com",
        "phone_number": "9876543210",
        "address": "Bengaluru, Karnataka",
    }

    doctors = send_request("/api/doctors/", "GET")
    doctor = next(
        (
            item for item in (doctors or [])
            if item["email"] == doctor_data["email"]
        ),
        None,
    )

    if not doctor:
        doctor = send_request("/api/doctors/", "POST", doctor_data)

    if doctor:
        mapping = send_request(
            "/api/mappings/",
            "POST",
            {
                "patient": patient_id,
                "doctor": doctor["id"],
            },
        )

        send_request("/api/mappings/", "GET")
        send_request(
            f"/api/mappings/patient/{patient_id}/",
            "GET",
        )
