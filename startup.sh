#!/bin/bash
echo "Starting deployment script"
python -m pip install --upgrade pip
echo "Installing requirements"
pip install -r requirements.txt
echo "Starting application with Gunicorn"
#gunicorn --bind=0.0.0.0 --timeout 600 --log-level debug main:app
gunicorn --bind=0.0.0.0:8000 --timeout 600 main:app