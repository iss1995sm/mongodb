# Recursos http://gpd.sip.ucm.es/rafa/docencia/nosql/IntroPython.html


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


collection.update_one({"nombre": "uno"}, {'$set':{"email": "Otro email"}})