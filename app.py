from flask import Flask, jsonify, request
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
app = Flask(__name__)
uri = "mongodb+srv://markmareyessa:1OZcOwu5K0MzK6dA@cluster0.4fggzux.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi('1'))

test_db = client.new_db
mycol = test_db.test
# x = test_db.list_collection_names()
# print(x)

# # create/use a new collection

# # insert a document (this actually creates the db + collection)
# doc = {"name": "first record", "ID": 123}
# result = mycol.insert_one(doc)
def SelectALL():
    docs = list(mycol.find({}, {"_id": 0}))  # exclude _id for clean JSON
    return docs
# def insert_new(doc):
#     collection =  test_db.test
#     inserted_id = collection.insert_one(doc).inserted_id
#     print(inserted_id)
    
# doc = {"name": "Mark", "ID": 1234}
@app.route('/')
def home():
    return jsonify(SelectALL())

@app.route('/insert/<name>/<int:ID>', methods=['GET'])
def insert_with_path(name, ID):
    doc = {"name": name, "ID": ID}
    mycol.insert_one(doc)
    return "Inserted Successfully"