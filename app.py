from flask import Flask, jsonify, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
app = Flask(__name__)
# x = test_db.list_collection_names()
# print(x)

# # create/use a new collection

# # insert a document (this actually creates the db + collection)
# doc = {"name": "first record", "ID": 123}
# result = mycol.insert_one(doc)
# def insert_new(doc):
#     collection =  test_db.test
#     inserted_id = collection.insert_one(doc).inserted_id
#     print(inserted_id)
    
# doc = {"name": "Mark", "ID": 1234}
@app.route('/')
def home():
    return "Hello"
