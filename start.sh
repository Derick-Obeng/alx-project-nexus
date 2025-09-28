#!/bin/bash
set -e

# make sure we are in the manage.py folder
cd /app/thepoll

echo "DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE"
echo "PORT=${PORT:-8080}"

echo "Running migrations..."
python3 manage.py migrate --noinput

echo "Collecting static files..."
python3 manage.py collectstatic --noinput

echo "Starting Gunicorn..."
# use ${PORT:-8080} to default to 8080 if platform didn't set $PORT
gunicorn thepoll.wsgi:application --bind 0.0.0.0:${PORT:-8080} --workers 2
