echo "Welcome to the item drop watcher!"

echo "Starting virtual environment" 

python3 -m venv venv

. venv/bin/activate

pip install -r requirements.txt > requirements_install_log.txt

python src/main.py

echo "Goodbye!"

deactivate