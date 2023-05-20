#!/bin/bash

if [ "$DEBUG"==True ]; then
    python manage.py makemigrations
    python manage.py migrate
    python manage.py load_data
    python manage.py create_superuser
    python manage.py collectstatic --no-input
fi

gunicorn tree_menu.wsgi:application --bind 0:8000