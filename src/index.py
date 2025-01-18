#importamos la configuracion de la aplicación desde app
from app import app

#Comprobamos el nombre de la aplicación
if __name__ == '__main__':
    app.run(debug = True, port = 5000)
