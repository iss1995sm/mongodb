# Instalar MongoDB
https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-20-04-es


# Instalar mongodb COMPASS (visualización de colecciones)
https://www.digitalocean.com/community/tutorials/how-to-use-mongodb-compass


# Comandos de mongodb
- $ mongo || - $ mongosh (en versión 5.0.6)
- $ show dbs
- $ use 'nombreDeDB'
- $ show collections
- $ db.'nombreDecoleccion'.find()



# Instalar pymongo
pip3 install pymongo


# Recursos
- PyMongo, Python & Mongodb (Fazt Code): https://www.youtube.com/watch?v=NVoeBH0uBHo

- FastAPI & Mongodb RESTAPI CRUD (Fazt Code): https://www.youtube.com/watch?v=4e2VW3Nu-64





# Actualizar MongoDB a 5.0.6
- $ curl -fsSL https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -

- $ apt-key list

- $ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list

- $ sudo apt update

- $ sudo apt install mongodb-org

- $ mongo --version

- $ sudo systemctl start mongod.service

