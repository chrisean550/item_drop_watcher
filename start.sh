#!/bin/bash

echo "Welcome to the item drop watcher!"

echo "Starting virtual environment" 

python3 -m venv venv

. venv/bin/activate

echo "Virtual environment started"

echo "Installing dependencies..."

pip install -r requirements2.txt

echo "Dependencies installed"

python src/main.py "prod"

echo "Goodbye!"

deactivate