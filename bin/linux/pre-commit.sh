#!/usr/bin/env bash

set -e

source venv/bin/activate

cd backend

poetry run isort .

poetry run black .

cd ../frontend

yarn format

yarn lint

cd ../

git add .
