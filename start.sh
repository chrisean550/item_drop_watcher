#!/bin/bash

echo "Welcome to the item drop watcher!"

echo "Starting virtual environment" 

python3 -m venv venv

. venv/bin/activate

echo "Virtual environment started"

echo "Installing dependencies..."

pip install -r requirements.txt > requirements_install_log.txt

echo "Dependencies installed.. check requirements_install_log.txt for output"

python src/main.py "prod"

echo "Goodbye!"

deactivate