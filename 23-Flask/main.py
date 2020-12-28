# Importar Flask
from flask import Flask, redirect, url_for, render_template
# Redirect => Para redirigir a otra pagina
# Url_for => podemos llamar a la url por el nombre de la funcion.
# Render_template => Para pooder renderizar plantillas.

# Para importar fecha(Context Processors)
from datetime import datetime


# Crear la app general de Flask
app=Flask(__name__)
# (Context Processors)
@app.context_processor
def date_now():
    return {
        'now':datetime.utcnow()
    }

# EndPoints




# Crear ruta index
@app.route('/')
def index():
    edad=150
    return render_template('index.html',
                edad=edad,
                dato1="Valor1",
                dato2="Valor2",
                lista=["Uno","Dos","Tres","Cuatro","Cinco"]
    )






# Para que los valores sean opcionales en ruta informacion.
@app.route('/informacion')
# Crear ruta Informacion
@app.route('/informacion/<string:nombre>')
@app.route('/informacion/<string:nombre>/<string:apellidos>')
def informacion(nombre=None,apellidos=None):
    txt=""
    if nombre != None and apellidos != None :
        txt =f"Bienvenido {nombre} {apellidos}"
    elif apellidos == None:
        txt =f"Bienvenido {nombre}"
    elif nombre == None:
        txt =f"Bienvenido {apellidos}"

    return render_template('informacion.html',txt=txt)


# Crear ruta Contacto
@app.route('/contacto')
@app.route('/contacto/<redireccion>')
def contacto(redireccion=None):
    # 1. Hay que importar de Flask redirect y url_for.
    # 2. Al usar url_for podemos llamar a la url por el nombre de la funcion que ejecuta, no por la url.
    # 3. Este IF redirige a la pagina 'lenguajes-de-programacion', sí el parametro pasado por la url es True.
    if redireccion is not None:
        return redirect(url_for('lenguajes'))

    return render_template('contacto.html')


# crear ruta de lenguales de Pro
@app.route('/lenguajes-de-programacion')
def lenguajes():

    return render_template('lenguajes.html')





# Identifica que el nombre de la aplicacion de flask  sea de un proyecto de Flask.
if __name__ == '__main__':
    # Comprueba que funciona el srvidor correctamente y ademas cuando hacemos un cambio recarga y se reinicia automaticamente
    app.run(debug=True)