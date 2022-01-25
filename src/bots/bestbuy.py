from selenium.webdriver.common.by import By
from bots.bot import Bot
from bs4 import BeautifulSoup

class BestBuy(Bot):

    def __init__(self, username, password, db, msg):
        self.url = "https://www.bestbuy.com/"
        self.driver = ''
        self.username = username
        self.password = password
        self.store = 'BestBuy'
        self.db = db
        self.msg = msg
    
    # Connects to store and navigates to desired webpage
    def connect(self):
        self.driver = Bot.open_browser()
        self.driver.get(self.url)
        self.__nav_to_saved()
    
    # Checks the current status on items in saved for later
    def watch(self):
        self.driver.refresh()
        items = self.__get_items()
        self.__check_availablity(items)
        Bot.wait(5, 10)

    
    def close(self):
        try:
            self.driver.close()
            self.driver.quit()
        except:
            pass

    # From the home page it signs in to account and accesses saved page
    def __nav_to_saved(self):

        print('Navigating to saved items')
        # Navigating to signin page
        self.__clear_blockers()
        self.driver.find_element(By.CLASS_NAME, 'account-button').click()
        self.driver.find_element(By.CLASS_NAME, 'sign-in-btn').click()
        Bot.wait()
        
        print('Entering signin information')
        # Entering signin info
        self.driver.find_element(By.ID, 'fld-e').send_keys(self.username)
        self.driver.find_element(By.ID, 'fld-p1').send_keys(self.password)
        Bot.wait()
        self.driver.find_element(By.CLASS_NAME, 'cia-form__controls__submit').click()
        
        print('On saved items page')
        # Navigating to saved for later page
        self.driver.find_element(By.CLASS_NAME, 'savedItems-button').click()
        self.driver.find_element(By.CLASS_NAME, 'see-all-link').click()

    # Uses BS4 to parse page html and get saved items
    def __get_items(self):
        Bot.wait()
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        items = soup.find_all('div', class_='grid-card-content')
        return items

    # Checks each item saved for availability
    def __check_availablity(self, items):
        for item in items:
            i = BeautifulSoup(str(item), 'html.parser')
            title = i.find('a', class_='title')
            status = i.find('button', class_='add-to-cart-button' )
            title = BeautifulSoup(str(title), 'lxml').text
            status = BeautifulSoup(str(status), 'lxml').text
            if(status == 'Add to Cart'):
                Bot.available(title, self.store, self.db, self.msg)
            else:
                Bot.unavailable(title, self.store, self.db)

    # Clears any overlays that may prevent clicks
    # might want to try a try catch loop that automates this
    def __clear_blockers(self):
        self.driver.execute_script("""
            return document.getElementsByClassName('c-modal-grid')[0].remove();
        """)
        self.driver.execute_script("""
            return document.getElementsByClassName('c-modal-window')[0].remove();
        """)
        self.driver.execute_script("""
            return document.getElementsByClassName('c-overlay-fullscreen')[0].remove();
        """)
        