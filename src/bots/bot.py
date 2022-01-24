import datetime
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from random import randint
from time import sleep

DRIVER_PATH = './geckodriver64'
HEADLESS = True
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


    # Actions to carry out if item is avaliable    
    def avaliable(item, store, db):
        current_time = datetime.datetime.now()
        date = str(current_time.month)+'-'+str(current_time.day)+'-'+str(current_time.year)
        time = str(current_time.hour)+':'+str(current_time.minute)

        data = {
            'item':item,
            'store':store,
            'last_avaliable': date+" "+time
        }

        # Prints status and updates "Last Avaliablity" cluster
        print('\033[1;32;40m'+item+' is AVAILABLE at '+store+' as of '+time+' on '+date+'\033[0;0m')
        db.update_last_avaliablity(data)

        # Updates "Current Avaliablity" cluster
        data.update({'status': 'In Stock'})
        db.update_current_avaliablity(data)

    # Actions to carry out if an item is unavaliable
    def unavaliable(item, store, db):
        current_time = datetime.datetime.now()
        date = str(current_time.month)+'-'+str(current_time.day)+'-'+str(current_time.year)
        time = str(current_time.hour)+':'+str(current_time.minute)

        data = {
            'item':item,
            'store':store,
            'last_avaliable': date+" "+time
        }

        # Prints status
        print('\033[1;31;40m'+item+' is UNAVAILABLE at '+store+' as of '+time+' on '+date+'\033[0;0m')

        # Updates "Current Avaliablity" cluster
        data.update({'status': 'Unavaliable'})
        db.update_current_avaliablity(data)


