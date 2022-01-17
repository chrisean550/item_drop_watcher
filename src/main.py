from ast import Try
from item import item
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import json
import time
from random import randint

DRIVER_PATH = './geckodriver'
active = True

def _main():
    # Configures headless browser
    print('Starting headless browser..')
    options = Options()
    options.headless = True
    service = Service(executable_path = DRIVER_PATH)
    driver = webdriver.Firefox(service=service, options=options)
    print('Browser has successfully opened')

    # Loads in json file with desired items
    with open('items.json', 'r') as file:
        data = json.load(file)

    # Creates object list with each item
    items = []
    for i in data['items']:
        items.append(item(i['item'], i['store'], i['url'], driver))

    # Check each items stock iteratively
    while active:
        for i in items:
            i.connect()
            i.check_inventory()
            time.sleep(randint(1, 6))

try:
    _main()
except KeyboardInterrupt:
    print('\nClosing program')
    

