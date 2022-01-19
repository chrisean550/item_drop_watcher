from mongo import MongoConnection
from dotenv import load_dotenv
import os

load_dotenv()

uri =  os.environ.get('MONGO_URI')
timeout = 5000

db = MongoConnection(uri, timeout)
db.connect()