
import json
import urllib.request
import urllib.error
import uuid

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

            return {
                "status": response.status,
                "data": json.loads(result) if result else None,
            }

    except urllib.error.HTTPError as error:
        print(f"\n{method} {path}")
        print("Status:", error.code)
        print(error.read().decode("utf-8"))

        return {
            "status": error.code,
            "data": None,
        }

    except urllib.error.URLError as error:
        print("\nCould not connect to the server.")
        print(error)

        return None


# 1. Create a doctor using a unique email
unique_email = f"doctor_{uuid.uuid4().hex[:8]}@example.com"

doctor_data = {
    "name": "Dr. Test Doctor",
    "specialization": "Cardiology",
    "email": unique_email,
    "phone_number": "9876543210",
    "address": "Test Address",
}

doctor_result = send_request(
    "/api/doctors/",
    "POST",
    doctor_data,
)

if doctor_result and doctor_result["status"] == 201:
    doctor = doctor_result["data"]
    doctor_id = doctor["id"]

    print("\nPASS: Doctor created successfully.")

    # 2. List all doctors
    send_request("/api/doctors/", "GET")

    # 3. Retrieve the created doctor
    send_request(f"/api/doctors/{doctor_id}/", "GET")

    # 4. Update the doctor
    updated_data = {
        **doctor_data,
        "name": "Dr. Test Doctor Updated",
    }

    update_result = send_request(
        f"/api/doctors/{doctor_id}/",
        "PUT",
        updated_data,
    )

    if update_result and update_result["status"] == 200:
        print("\nPASS: Doctor updated successfully.")

    # 5. Delete the test doctor
    delete_result = send_request(
        f"/api/doctors/{doctor_id}/",
        "DELETE",
    )

    if delete_result and delete_result["status"] == 204:
        print("\nPASS: Doctor deleted successfully.")
    else:
        print("\nCHECK: Doctor deletion did not return status 204.")

    print("\nDoctor test sequence completed.")

else:
    print(
        "\nDoctor creation failed, so the remaining "
        "tests were skipped."
    )
