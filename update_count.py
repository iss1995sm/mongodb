import pymongo
from pymongo import MongoClient
import json
from datetime import datetime
import time

client = MongoClient('mongodb://localhost:27017/')
ObjectId = datetime.now()


db = client.Nosql_Anuncios

collection = db.Nosql_Clients

db = client['Nosql_Anuncios']

collection = db['Nosql_Clients']


collection.update_one({'Nombre': 'uno'}, {'$set': {'Nombre':'tres'}})


count = collection.count_documents({})
print(count)