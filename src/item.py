from time import time
from bs4 import BeautifulSoup
import datetime


class item:
    def __init__(self, item, store, url, driver, page_source=''):
        self.item = item
        self.store = store
        self.url = url
        self.driver = driver
        self.page_source = page_source

    # Makes connection to desired webpage of console
    def connect(self):
        self.driver.get(self.url)
        self.page_source = self.driver.page_source

    # Chooses the approptiate function to use to check inventory status
    def check_inventory(self):
        if self.page_source == '':
            print('No page source found.. please make connection first')
            return
        
        if self.store == 'bestbuy':
            self.__best_buy()
        else:
            print('This store is incompatable')

    def __best_buy(self):
        soup = BeautifulSoup(self.page_source, 'html.parser')
        output = soup.find_all('button', class_='add-to-cart-button')[0]
        status = BeautifulSoup(str(output), 'lxml')
        if status.text == "Sold Out":
            self.__print_status(False)
        else:
            self.__print_status(True)

    def __print_status(self, status):
        current_time = datetime.datetime.now()
        date = str(current_time.month)+'-'+str(current_time.day)+'-'+str(current_time.year)
        time = str(current_time.hour)+':'+str(current_time.minute)

        if status:
            print('\033[1;32;40m'+self.item+' is AVAILABLE at '+self.store+
            ' as of '+time+' on '+date+'\033[0;0m')
        else:
            print('\033[1;31;40m'+self.item+' is UNAVAILABLE at '+self.store+
            ' as of '+time+' on '+date+'\033[0;0m')
        
