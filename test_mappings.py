
import json
import urllib.request
import urllib.error

BASE_URL = "http://127.0.0.1:8000"
ACCESS_TOKEN = input(
    "Paste your current JWT access token: "
).strip().strip('"').strip("'")


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

    except urllib.error.URLError as error:
        print(f"\nCould not connect to {BASE_URL}")
        print(error)
        return None


# 1. Create a new patient
patient_data = {
    "name": "Rahul Sharma",
    "age": 29,
    "gender": "Male",
    "address": "Mumbai, Maharashtra",
    "phone_number": "9876543210",
}

patient = send_request("/api/patients/", "POST", patient_data)

if patient and "id" in patient:
    patient_id = patient["id"]

    # 2. Find an existing doctor or create one
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
            item
            for item in (doctors or [])
            if item["email"] == doctor_data["email"]
        ),
        None,
    )

    if not doctor:
        doctor = send_request(
            "/api/doctors/", "POST", doctor_data
        )

    # 3. Create a patient-doctor mapping
    if doctor and "id" in doctor:
        mapping = send_request(
            "/api/mappings/",
            "POST",
            {
                "patient": patient_id,
                "doctor": doctor["id"],
            },
        )

        # 4. List all mappings
        send_request("/api/mappings/", "GET")

        # 5. List doctors assigned to this patient
        # Updated URL to match the assignment
        send_request(f"/api/mappings/{patient_id}/", "GET")

        # 6. Check duplicate prevention only if mapping creation succeeded
        if mapping and "id" in mapping:
            send_request(
                "/api/mappings/",
                "POST",
                {
                    "patient": patient_id,
                    "doctor": doctor["id"],
                },
            )
