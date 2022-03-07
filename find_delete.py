'''
Recursos: 
    http://gpd.sip.ucm.es/rafa/docencia/nosql/IntroPython.html
    https://www.youtube.com/watch?v=NVoeBH0uBHo
'''

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


results = collection.find()
for result in results:
    print('EL DICCIONARIO ENTERO: ', result, '\n')
    print('UN VALOR CONCRETO:', result['Nombre'])


'''FIND EXAMPLES'''
# results = collection.find({'precio' : 300})

# results = collection.find_one({'Nombre' : 'uno})

# results = collection.find({'precio' : 300})

# collection.find_one({"nombre": "uno"}, {'$set':{"email": "Otro email"}})


'''DELETE EXAMPLES'''
# collection.delete_one({'Nombre' : 'uno})
# collection.delete_many({})
