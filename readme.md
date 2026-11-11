# MtaaHomes
A Django-based rental listing marketplace for MUT students and the
surrounding Murang'a community.
## Features in Phase 1- House seeker and landlord registration- Landlord property submissions- Property photo uploads- Admin approval and rejection- Public display of approved listings only
## Local setup (Windows PowerShell)
1. Clone the repository.
2. Create and activate a virtual environment:
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
3. Install dependencies:
   python -m pip install "Django>=5.2,<6.2" Pillow
   4. Apply migrations:
   python manage.py migrate
5. Create an admin:
   python manage.py createsuperuser
6. Run:
   python manage.py runserver
Open http://127.0.0.1:8000/
## Development notes- SQLite is for local development only.- Never commit .env, db.sqlite3, .venv, media uploads, or secrets.- Only approved listings are shown publicly