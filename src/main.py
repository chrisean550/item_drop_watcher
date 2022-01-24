from mongo import MongoConnection
from dotenv import load_dotenv
from bots.bestbuy import BestBuy
import sys
import os

load_dotenv()

DATABASE = os.environ.get('MONGO_URI')
BB_USR = os.environ.get('BESTBUY_USERNAME')
BB_PWD = os.environ.get('BESTBUY_PASSWORD')

def _main():

    # Connecting to mongodb
    print("Connecting to database...")
    db = MongoConnection(DATABASE)
    db.connect()

    print("Connecting Bestbuy bot..")
    global bot1
    bot1 = BestBuy(BB_USR, BB_PWD, db)
    bot1.connect()
    
    while True:
        bot1.watch()

    
            

try:
    _main()
except KeyboardInterrupt:
    print('\nClosing program')
    

