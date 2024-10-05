#!/usr/bin/env bash

set -e

cd frontend

yarn install

cd ../

python -m venv venv

source venv/bin/activate

cd backend

poetry install

./start-migrate.sh

wait
