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


nombre = input('introduce tu nombre: ',)
email = input('introduce tu email: ',)
psw = input('introduce tu contraseña: ',)
via = input('introduce tu calle ',)
numero = input('introduce tu numero de portal: ',)
ciudad = input('introduce tu ciudad: ',)
cp = input('introduce tu CP: ',)
direccion = [via, numero, ciudad, cp]

collection.insert_one({"_id": ObjectId,
                        "Nombre": nombre,
                        "Email": email, 
                        "password": psw,
                        "Dirección": direccion})


cliente_uno = {'Nombre': 'nombre1'}
cliente_dos = {'Nombre': 'nombre2'}

collection.insert_many([cliente_uno, cliente_dos])
