#!/usr/bin/env bash

set -e

echo -e "\033[0;32m[INFO]\033[0;0m Starting redis..."

echo -e "\033[0;32m[INFO]\033[0;0m Starting rabbit..."

echo -e "\033[0;32m[INFO]\033[0;0m Starting postgres..."

echo -e "\033[0;32m[INFO]\033[0;0m Starting kafka..."

echo -e "\033[0;32m[INFO]\033[0;0m Starting frontend..."

echo -e "\033[0;32m[INFO]\033[0;0m Starting backend..."

echo -e "\033[0;32m[INFO]\033[0;0m Starting celery..."

echo -e "\033[0;32m[INFO]\033[0;0m Starting flower..."

wait
