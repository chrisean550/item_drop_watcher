import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

DRIVER_PATH = './geckodriver64'
HEADLESS = True

class Bot:

    def open_browser():
        # Configures headless browser
        print('Starting headless browser..')

        options = Options()
        options.headless = HEADLESS
        service = Service(executable_path = DRIVER_PATH)
        driver = webdriver.Firefox(service=service, options=options)

        print('Browser has successfully opened')

        return driver

    # Actions to carry out if item is avaliable    
    def avaliable():
        current_time = datetime.datetime.now()
        date = str(current_time.month)+'-'+str(current_time.day)+'-'+str(current_time.year)
        time = str(current_time.hour)+':'+str(current_time.minute)

        data = {
            'item':self.item,
            'store':self.store,
            'url':self.url,
            'last_avaliable': date+" "+time
        }

        print('\033[1;32;40m'+self.item+' is AVAILABLE at '+self.store+' as of '+time+' on '+date+'\033[0;0m')
        self.db.update_last_avaliablity(data)

        data.update({'status': 'In Stock'})
        self.db.update_current_avaliablity(data)

    # Actions to carry out if an item is unavaliable
    def unavaliable():
        current_time = datetime.datetime.now()
        date = str(current_time.month)+'-'+str(current_time.day)+'-'+str(current_time.year)
        time = str(current_time.hour)+':'+str(current_time.minute)

        data = {
            'item':self.item,
            'store':self.store,
            'url':self.url,
            'last_avaliable': date+" "+time
        }

        print('\033[1;31;40m'+self.item+' is UNAVAILABLE at '+self.store+' as of '+time+' on '+date+'\033[0;0m')

        data.update({'status': 'Unavaliable'})
        self.db.update_current_avaliablity(data)


