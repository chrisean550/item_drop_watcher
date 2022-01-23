from mongo import MongoConnection
from dotenv import load_dotenv
from bots.bestbuy import BestBuy
import sys
import os

load_dotenv()

DATABASE = os.environ.get('MONGO_URI')

def _main():

    # Connecting to mongodb
    print("Connecting to database...")
    db = MongoConnection(DATABASE)
    db.connect()

    print("Connecting Bestbuy bot..")
    bot1 = BestBuy()
    bot1.connect()

    
            

try:
    _main()
except KeyboardInterrupt:
    print('\nClosing program')
    

