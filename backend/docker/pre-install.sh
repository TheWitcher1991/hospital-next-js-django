#!/bin/sh

echo "Installing linux dependencies"

apt-get update

apt-get install -y --no-install-recommends \
    netcat-traditional \
    libpq-dev \
    build-essential \
    postgresql-client \
    redis-server \
    rabbitmq-server \
    nginx \
    supervisor

apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
