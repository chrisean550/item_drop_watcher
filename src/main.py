from smtplib import SMTP_PORT
from mongo import MongoConnection
from dotenv import load_dotenv
from bots.bestbuy import BestBuy
from message import Message
import sys
import os

load_dotenv()

DATABASE = os.environ.get('MONGO_URI')
BB_USR = os.environ.get('BESTBUY_USERNAME')
BB_PWD = os.environ.get('BESTBUY_PASSWORD')
SMTP = os.environ.get('SMTP')
SMTP_PORT = os.environ.get('SMTP_PORT')
SMTP_EMAIL = os.environ.get('SMTP_EMAIL')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
SMS_GATEWAY = os.environ.get('SMS_GATEWAY')

Bots = []

def _main():

    # Connecting to mongodb
    print('Connecting to database..')
    db = MongoConnection(DATABASE)
    db.connect()

    print('Starting SMTP server..')
    msg = Message(SMTP_EMAIL, SMTP_PASSWORD, SMS_GATEWAY, SMTP, SMTP_PORT)
    msg.start()

    print('Connecting Bestbuy bot..')
    global bot1
    Bots.append(BestBuy(BB_USR, BB_PWD, db, msg))
    
    for bot in Bots:
        bot.connect()
    
    while True:
        for bot in Bots:
            bot.check_status()

def end_program():
    for bot in Bots:
        bot.shut_down()

    
            

try:
    _main()
except KeyboardInterrupt:
    print('\nClosing program')
    end_program()
    

