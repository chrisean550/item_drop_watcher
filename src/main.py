from item import Item
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from mongo import MongoConnection
from dotenv import load_dotenv
import json
from random import randint
import sys
import os

load_dotenv()


# Determines what firefox driver to use for system
if sys.argv[1] == "dev":
    DRIVER_PATH = './geckodriver64'
else:
    DRIVER_PATH = './geckodriver'

HEADLESS = True
DATABASE = os.environ.get('MONGO_URI')

active = True

def _main():
    
    # Configures headless browser
    print('Starting headless browser..')
    options = Options()
    options.headless = HEADLESS
    service = Service(executable_path = DRIVER_PATH)
    driver = webdriver.Firefox(service=service, options=options)
    print('Browser has successfully opened')

    # Loads in json file with desired items
    with open('items.json', 'r') as file:
        data = json.load(file)

    # Connecting to mongodb
    db = MongoConnection(DATABASE)
    db.connect()
    
    # Creates object list with each item
    items = []
    for i in data['items']:
        items.append(Item(i['item'], i['store'], i['url'], driver, db))

    # Check each items stock iteratively
    while active:
        for i in items:
            i.connect()
            i.check_inventory()
            

try:
    _main()
except KeyboardInterrupt:
    print('\nClosing program')
    

