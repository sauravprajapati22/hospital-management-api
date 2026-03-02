# Hospital Management API

A role-based Hospital Management REST API built using Django REST Framework.

## Features
- Custom User (Doctor / Patient)
- JWT Authentication
- Role-Based Permissions
- Appointment Booking System
- Pagination, Search, Ordering

## Tech Stack
- Django
- Django REST Framework
- SimpleJWT
- SQLite (Development)

## API Endpoints

POST   /api/accounts/register/
POST   /api/accounts/login/

POST   /api/appointments/
GET    /api/appointments/me/
GET    /api/appointments/doctor/

## Setup Instructions

1. Clone repository
2. Create virtual environment
3. Install dependencies:
   pip install -r requirements.txt
4. Run migrations:
   python manage.py migrate
5. Run server:
   python manage.py runserver