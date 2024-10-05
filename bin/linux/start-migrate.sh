#!/usr/bin/env bash

set -e

source venv/bin/activate

cd backend

python manage.py makemigrations
python manage.py migrate --check
