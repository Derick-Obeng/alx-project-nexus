# alx-project-nexus

## Project Overview

This is a Django-based poll system with REST API support and Swagger documentation. It allows users to create polls, vote, and view real-time results.

## Setup Instructions

1. **Clone the repository:**
 ```sh
 git clone <repo-url>
 cd alx-project-nexus
 ```

2. **Create and activate a virtual environment:**
 ```sh
 python -m venv .venv
 # On Windows:
 .venv\Scripts\activate
 # On Mac/Linux:
 source .venv/bin/activate
 ```

3. **Install dependencies:**
 ```sh
 pip install django djangorestframework drf-yasg
 ```

4. **Apply migrations:**
 ```sh
 cd thepoll
 python manage.py makemigrations
 python manage.py migrate
 ```

5. **Run the development server:**
 ```sh
 python manage.py runserver
 ```

6. **Access the app:**
 - Polls: <http://127.0.0.1:8000/poll/>
 - Admin: <http://127.0.0.1:8000/admin/>
 - Swagger docs: <http://127.0.0.1:8000/swagger/>

## Example Usage

- **Create a poll:** Use the Django admin or API endpoint to add a new poll and choices.
- **Vote:** Go to `/poll/<poll_id>/` and submit your vote.
- **View results:** Go to `/poll/<poll_id>/results/` to see real-time results with progress bars.

## Project Structure

- `thepoll/` - Main Django project folder
- `poll/` - Polls app (models, views, templates)
- `media/` - Uploaded images for choices
- `templates/poll/` - HTML templates for poll pages

## Notes

- Uses SQLite by default (see `thepoll/settings.py` for DB config)
- Add your own settings for production (e.g., DEBUG, ALLOWED_HOSTS)
