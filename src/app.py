#Importamos los modulos  a emplear
from flask import Flask
from routes.users import users
from routes.auth import auth

#Definimos una variable para asignar la instancia de la clase
app = Flask(__name__)

app.register_blueprint(users)
app.register_blueprint(auth)