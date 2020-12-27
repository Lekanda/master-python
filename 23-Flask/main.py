# Importar Flask
from flask import Flask

# Crear la app general de Flask
app=Flask(__name__)

# Crear ruta index
@app.route('/')
def index():
    return "Aprendiendo FLASK"

# Crear ruta Informacion
@app.route('/informacion/<nombre>/<apellidos>')
def informacion(nombre,apellidos):

    return f"""
                <h1>Informacion</h1>
                <p>Esta es la pagina de informacion</p>
                <h3>Usuario: {nombre} {apellidos}</h3>
            """

# Crear ruta Contacto
@app.route('/contacto')
def contacto():

    return "<h1>Contacto</h1>"

# crear ruta de lenguales de Pro
@app.route('/lenguajes-de-programacion')
def lenguajes():

    return "<h1>Lenguajes de Programacion</h1>"





# Identifica que el nombre de la aplicacion de flask  sea de un proyecto de Flask.
if __name__ == '__main__':
    # Comprueba que funciona el srvidor correctamente y ademas cuando hacemos un cambio recarga y se reinicia automaticamente
    app.run(debug=True)