#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run database migrations
echo "Running database migrations..."
python manage.py migrate 

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic
