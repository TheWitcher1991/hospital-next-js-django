#!/bin/sh

echo "Running makes migrations..."
python manage.py makemigrations

echo "Running migrations..."
python manage.py migrate --skip-checks

echo "Loading fixtures..."

# ...

echo "Creating superuser..."
if [ "$DJANGO_SUPERUSER_USERNAME" ] && [ "$DJANGO_SUPERUSER_EMAIL" ] && [ "$DJANGO_SUPERUSER_PASSWORD" ] && [ "$DJANGO_SUPERUSER_PHONE" ]; then
    python manage.py createsuperuser --no-input || true
fi

echo "Collecting static files..."
python manage.py collectstatic --noinput

exec "$@"