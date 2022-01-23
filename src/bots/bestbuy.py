from bots.bot import Bot

class BestBuy(Bot):

    def __init__(self):
        self.url = "https://www.bestbuy.com/"
        self.driver = ''
    
    def connect(self):
        self.driver = Bot.open_browser()
        self.driver.get(self.url)
        print(self.driver.title)



    def __best_buy(self):
        soup = BeautifulSoup(self.page_source, 'html.parser')
        output = soup.find_all('button', class_='add-to-cart-button')[0]
        status = BeautifulSoup(str(output), 'lxml')
        if status.text == "Sold Out" or status.text == "Unavailable Nearby":
            self.__avaliable_action(False)
        else:
            self.__avaliable_action(True)