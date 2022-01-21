from unittest import result
import pymongo

class MongoConnection:

    def __init__(self, uri, timeout=5000, client=''):
        self.uri = uri
        self.timeout = timeout
        self.client = client

    def connect(self):
        self.client = pymongo.MongoClient(self.uri,
         serverSelectionTimeoutMS=self.timeout)

        try:
            self.client.server_info()
            #print("Successfull connection")
        except Exception:
            print("Failed to connect to server")

    def update_last_avaliablity(self, data):

        # Connect to desired cluster
        db = self.client.item_drop
        collection = db.last_avaliablity

        # Construct query
        query = {'item': data['item'], 'store': data['store']}
        
        # Update if item exist and insert if not
        if self.__item_exist(collection, query):
            collection.update_one(query, {"$set": data}, upsert=True)
        else:
            collection.insert_one(data)

    def update_current_avaliablity(self, data):
        # Connect to desired cluster
        db = self.client.item_drop
        collection = db.current_avaliablity

        # Construct query
        query = {'item': data['item'], 'store': data['store']}
        
        # Update if item exist and insert if not
        if self.__item_exist(collection, query):
            collection.update_one(query, {"$set": data}, upsert=True)
        else:
            collection.insert_one(data)

    def __item_exist(self, collection, query):
        results = collection.find_one(query)
        if results == "None":
            return False
        else: 
            return True