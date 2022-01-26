import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from random import randint
from time import sleep
import sys

if sys.argv[1] == 'dev':
    HEADLESS = False
    DRIVER_PATH = './geckodriver64'
else:
    HEADLESS = True
    DRIVER_PATH = './geckodriver'

WAIT_TIME = 10

class Bot:

    # Opens and prepares browser for store
    def open_browser():
        options = Options()
        options.headless = HEADLESS
        service = Service(executable_path = DRIVER_PATH)
        driver = webdriver.Firefox(service=service, options=options)
        driver.implicitly_wait(WAIT_TIME)
        driver.delete_all_cookies()
        return driver
    
    # Randomized wait time to keep website from getting upset
    def wait(min=1, max=4):
        sleep(randint(min, max))


    # Actions to carry out if item is available    
    def available(item, store, db, msg):
        current_time = datetime.datetime.now()
        date = str(current_time.month)+'-'+str(current_time.day)+'-'+str(current_time.year)
        time = str(current_time.hour)+':'+str(current_time.minute)
        message = item+' is AVAILABLE at '+store+' as of '+time+' on '+date

        data = {
            'item':item,
            'store':store,
            'last_available': date+' '+time
        }

        # Sends message
        if(db.check_status(item, store) != 'In Stock'):
            msg.send_message(message)

        # Prints status and updates "Last Availablity" cluster
        print('\033[1;32;40m'+message+'\033[0;0m')
        db.update_last_availablity(data)

        # Updates "Current Availablity" cluster
        data.update({'status': 'In Stock'})
        db.update_current_availablity(data)

    # Actions to carry out if an item is unavailable
    def unavailable(item, store, db):
        current_time = datetime.datetime.now()
        date = str(current_time.month)+'-'+str(current_time.day)+'-'+str(current_time.year)
        time = str(current_time.hour)+':'+str(current_time.minute)
        message = item+' is UNAVAILABLE at '+store+' as of '+time+' on '+date

        data = {
            'item':item,
            'store':store,
            'last_available': date+' '+time
        }

        # Prints status
        print('\033[1;31;40m'+message+'\033[0;0m')

        # Updates "Current Availablity" cluster
        data.update({'status': 'Unavailable'})
        db.update_current_availablity(data)


