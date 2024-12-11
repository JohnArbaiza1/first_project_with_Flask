#Importamos los modulos 
from flask import Flask
from flask import render_template

#Definimos una variable para asignar la instancia de la clase
app = Flask(__name__)

#utilizamos el decorador route() para indicar a Flask qué URL debe activar nuestra función.
@app.route('/')
#Defiimos una funcion para que retornen nuestro template
def inicio():
    #Diccionario de dato que pasamos al layout 
    datos = {
        'titulo': 'First project with Flask ',
        'Mensaje': 'Hola Mundo'
    }
    return render_template('/Views/index.html', data = datos)

#Comprobamos el nombre de la aplicación
if __name__ == '__main__':
        app.run(debug = True, port = 5000)