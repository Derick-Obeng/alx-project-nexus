#!/bin/bash
set -e

export DJANGO_SETTINGS_MODULE=thepoll.thepoll.settings

echo "Running migrations..."
python3 thepoll/manage.py migrate --noinput

echo "Collecting static files..."
python3 thepoll/manage.py collectstatic --noinput

echo "Starting Gunicorn..."
gunicorn thepoll.thepoll.wsgi:application --bind 0.0.0.0:$PORT
