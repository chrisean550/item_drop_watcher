from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bots.bot import Bot
from bs4 import BeautifulSoup
import time

class BestBuy(Bot):

    def __init__(self):
        self.url = "https://www.bestbuy.com/"
        self.driver = ''
    
    def connect(self):
        self.driver = Bot.open_browser()
        self.driver.get(self.url)
        print(self.driver.title)
        self.__nav_to_saved()
    
    def __nav_to_saved(self):
        time.sleep(1)
        self.driver.execute_script("""
            return document.getElementsByClassName('c-modal-grid')[0].remove();
        """)
        self.driver.execute_script("""
            return document.getElementsByClassName('c-modal-window')[0].remove();
        """)
        self.driver.execute_script("""
            return document.getElementsByClassName('c-overlay-fullscreen')[0].remove();
        """)
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'account-button').click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'sign-in-btn').click()



    def __best_buy(self):
        soup = BeautifulSoup(self.page_source, 'html.parser')
        output = soup.find_all('button', class_='add-to-cart-button')[0]
        status = BeautifulSoup(str(output), 'lxml')
        if status.text == "Sold Out" or status.text == "Unavailable Nearby":
            self.__avaliable_action(False)
        else:
            self.__avaliable_action(True)