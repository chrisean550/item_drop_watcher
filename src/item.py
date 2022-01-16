from lib2to3.pgen2.driver import Driver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

DRIVER_PATH = './geckodriver'


class item:
    def __init__(self, item, store, url, wordbank):
        self.item = item
        self.store = store
        self.url = url
        self.wordbank = wordbank

    def connect(self):
        # Configures headless browser
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(executable_path=DRIVER_PATH, options=options)
        
        # Makes connection to webpage and prints title
        driver.get(self.url)
        print(driver.title)
        driver.close()