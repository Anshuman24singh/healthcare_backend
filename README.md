# Healthcare Backend API

A RESTful healthcare management backend built with Django, Django REST Framework, PostgreSQL, and JWT authentication. The API supports user registration, login, patient management, doctor management, and patient-doctor assignments.

## Features

- User registration and JWT-based authentication
- Patient CRUD operations
- Doctor CRUD operations
- Assign doctors to patients
- Retrieve doctors assigned to a specific patient
- PostgreSQL database integration
- Authenticated API endpoints and ownership restrictions
- Validation to prevent duplicate patient-doctor assignments

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- Simple JWT
- psycopg
- python-dotenv

## Project Structure

```text
healthcare_backend/
├── healthcare/
│   ├── settings.py
│   └── urls.py
├── users/
├── patients/
├── doctors/
├── mappings/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Prerequisites

- Python installed
- PostgreSQL installed and running
- Git (optional, for cloning the repository)

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Anshuman24singh/healthcare_backend.git
cd healthcare_backend
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root. Add your own values:

```env
SECRET_KEY=replace-with-a-new-secret-key
DEBUG=True
DB_NAME=healthcare_db
DB_USER=healthcare_user
DB_PASSWORD=your-local-database-password
DB_HOST=127.0.0.1
DB_PORT=5432
```

Do not commit `.env` or share its secrets publicly.

### 5. Create the PostgreSQL database

Using PostgreSQL, create a database named `healthcare_db` and a database user named `healthcare_user`. Grant the user the required privileges on the database.

Use the credentials configured in your `.env` file.

### 6. Apply migrations

```powershell
python manage.py migrate
```

### 7. Start the development server

```powershell
python manage.py runserver
```

The API will be available at:

`http://127.0.0.1:8000/`

## API Endpoints

Except for registration and login, endpoints require a valid JWT access token.

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/auth/register/` | Register a user |
| POST | `/api/auth/login/` | Obtain access and refresh tokens |

Example registration request:

```json
{
  "name": "Rahul Sharma",
  "email": "rahul@example.com",
  "password": "Use-A-Strong-Password-123!"
}
```

Login uses the email and password. The response contains JWT access and refresh tokens.

### Patients

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/patients/` | Create a patient |
| GET | `/api/patients/` | List your patients |
| GET | `/api/patients/<id>/` | Retrieve a patient |
| PUT | `/api/patients/<id>/` | Update a patient |
| PATCH | `/api/patients/<id>/` | Partially update a patient |
| DELETE | `/api/patients/<id>/` | Delete a patient |

Example patient request:

```json
{
  "name": "Rahul Sharma",
  "age": 29,
  "gender": "Male",
  "address": "Mumbai, Maharashtra",
  "phone_number": "9876543210"
}
```

Patients are associated with the authenticated user who creates them.

### Doctors

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/doctors/` | Create a doctor |
| GET | `/api/doctors/` | List doctors |
| GET | `/api/doctors/<id>/` | Retrieve a doctor |
| PUT | `/api/doctors/<id>/` | Update a doctor |
| PATCH | `/api/doctors/<id>/` | Partially update a doctor |
| DELETE | `/api/doctors/<id>/` | Delete a doctor |

Example doctor request:

```json
{
  "name": "Dr. Priya Sharma",
  "specialization": "Cardiology",
  "email": "priya@example.com",
  "phone_number": "9876543210",
  "address": "Bengaluru, Karnataka"
}
```

Authenticated users can list doctors, while modifications are restricted to the user who created the doctor.

### Patient-Doctor Mappings

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/mappings/` | Assign a doctor to a patient |
| GET | `/api/mappings/` | List your patient-doctor mappings |
| GET | `/api/mappings/patient/<patient_id>/` | Get doctors assigned to a patient |
| DELETE | `/api/mappings/<id>/` | Delete a mapping |

Example mapping request:

```json
{
  "patient": 1,
  "doctor": 1
}
```

The patient must belong to the authenticated user. Duplicate assignments are rejected.

## Authentication

After logging in, copy the `access` token from the response.

Include it in protected API requests using this HTTP header:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Use the access token for API requests. The refresh token can be used with the JWT token refresh endpoint if configured in the project.

## Testing

Run the Django configuration check:

```powershell
python manage.py check
```

Check whether migrations are missing:

```powershell
python manage.py makemigrations --check --dry-run
```

The project also contains Python scripts for exercising patient, doctor, and mapping endpoints. Start the Django server in one terminal, then run the relevant test script from another terminal.

## Security Notes

- Keep `.env` and database credentials private.
- Set `DEBUG=False` and configure suitable production security settings before deployment.
- Use HTTPS in production.
- Restrict allowed hosts and configure production database credentials securely.

## Author

Anshuman Singh

GitHub: [Anshuman24singh](https://github.com/Anshuman24singh)