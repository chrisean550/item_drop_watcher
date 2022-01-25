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
            print("Successfull connection")
        except Exception:
            print("Failed to connect to database")

    def update_last_availablity(self, data):

        # Connect to desired cluster
        db = self.client.item_drop
        collection = db.last_availablity

        # Construct query
        query = {'item': data['item'], 'store': data['store']}
        
        # Update if item exist and insert if not
        if self.__item_exist(collection, query):
            collection.update_one(query, {"$set": data}, upsert=True)
        else:
            collection.insert_one(data)

    def update_current_availablity(self, data):
        # Connect to desired cluster
        db = self.client.item_drop
        collection = db.current_availablity

        # Construct query
        query = {'item': data['item'], 'store': data['store']}
        
        # Update if item exist and insert if not
        if self.__item_exist(collection, query):
            collection.update_one(query, {"$set": data}, upsert=True)
        else:
            collection.insert_one(data)

    def check_status(self, item, store):
        # Connect to desired cluster
        db = self.client.item_drop
        collection = db.current_availablity

        # Construct query
        query = {'item': item, 'store': store}

        if self.__item_exist(collection, query):
            result = collection.find_one(query)
            return result['status']
        else:
            return 'Unkown'

    def __item_exist(self, collection, query):
        result = collection.find_one(query)
        if str(result) == "None":
            return False
        else: 
            return True