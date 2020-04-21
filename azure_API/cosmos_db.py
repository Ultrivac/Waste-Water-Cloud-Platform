
from pymongo import MongoClient
import os

URI = "cosmos db connection string here"
name = "username of db"
password = "cosmos db password string"

# provided database name and collection (both strings) return collection
# database and collection need to be valid resource names from azure cosmos db
def get_collection(database, collection):
    try:
        # use for local testing
        client = MongoClient(URI)
        db = client[database] # select the database
        db.authenticate(name=name, password=password)

        # use for deployed use and fill credentials
        # client = MongoClient(os.getenv("MONGOURL"))
        # db = client.test
        #db.authenticate(name=os.getenv("MONGO_USERNAME"),password=os.getenv("MONGO_PASSWORD"))

        my_collection = db[collection]
        return my_collection
    except:
        return None

# given a valid database name, a list of collections in that database is returned
def query_for_collections(database):
    try:
        # use for local testing
        client = MongoClient(URI)
        db = client[database] # select the database
        db.authenticate(name=name, password=password)
        # use for deployed use and fill credentials
        # client = MongoClient(os.getenv("MONGOURL"))
        # db = client.test
        #db.authenticate(name=os.getenv("MONGO_USERNAME"),password=os.getenv("MONGO_PASSWORD"))

        return db.list_collection_names()
    except:
        return None
