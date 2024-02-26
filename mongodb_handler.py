from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure


class MongoDBHandler:
    def __init__(self, connection_string, database):
        self.connection_string = connection_string
        self.database = database
        self.client = None
        self.db = None

    def connect(self):
        try:
            self.client = MongoClient(self.connection_string)
            self.client.server_info()
            self.db = self.client[self.database]
            print(f"Connected to MongoDB")
        except ConnectionFailure:
            raise ConnectionError("The connection to MongoDB has failed. Please check your configuration settings.")
        except ServerSelectionTimeoutError:
            raise ConnectionError("The MongoDB server is not responding")

    def insert_many(self, collection, documents):
        collection = self.db[collection]
        collection.insert_many(documents)
        print(f"Inserted {len(documents)} documents into {collection} collection")

    def close_connection(self):
        if self.client:
            self.client.close()
            print("Connection to MongoDB closed")
