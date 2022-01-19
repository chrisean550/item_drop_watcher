from sre_constants import SUCCESS
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
            print("Failed to connect to server")