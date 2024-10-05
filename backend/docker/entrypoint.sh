#!/bin/sh

echo "Running makes migrations..."
python manage.py makemigrations

echo "Running migrations..."
python manage.py migrate --skip-checks

echo "Loading fixtures..."

# ...

echo "Creating superuser..."
python manage.py initadmin

echo "Collecting static files..."
python manage.py collectstatic --noinput

exec "$@"