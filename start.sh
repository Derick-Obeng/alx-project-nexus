#!/bin/bash
set -e

# make sure we are in the manage.py folder
cd /app/thepoll

echo "DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE"
echo "PORT=${PORT:-8080}"

echo "Running migrations..."
python3 manage.py migrate --noinput

echo "Creating superuser if not exists..."
python3 manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(is_superuser=True).exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword123')
    print('Superuser created: admin / adminpassword123')
else:
    print('Superuser already exists')
"

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Starting Gunicorn..."
# use ${PORT:-8080} to default to 8080 if platform didn't set $PORT
gunicorn thepoll.wsgi:application --bind 0.0.0.0:${PORT:-8080} --workers 2
