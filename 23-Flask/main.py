# Importar Flask
from flask import Flask, redirect, url_for, render_template,request,flash
# Redirect => Para redirigir a otra pagina
# Url_for => podemos llamar a la url por el nombre de la funcion.
# Render_template => Para pooder renderizar plantillas.

# Para importar fecha(Context Processors)
from datetime import datetime

from flask_mysqldb import MySQL

# Crear la app general de Flask
app=Flask(__name__)

# LLave secreta para las sesiones.
# Error: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.
app.secret_key='clave_secreta_flask'

# Conexion a la DB
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'xa6nXxyZkaHENeJ3'
app.config['MYSQL_DB'] = 'proyectoflask'
# Mi MySQL esta en el puerto 3308. Diferente al curso
app.config['MYSQL_PORT'] = 3308
mysql = MySQL(app)



# Context Processors
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
    personas=['Paco','Pepe','Juan','Luis','Alberto']
    return render_template('index.html',
                edad=edad,
                dato1="Valor1",
                dato2="Valor2",
                lista=["Uno","Dos","Tres","Cuatro","Cinco"],
                personas=personas
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


# Ruta para crear coche desde formualrio
@app.route('/crear-coche', methods=['GET','POST'])
# methods=['GET','POST']) => Habilita los metodos GET y POST
def crear_coche():
    if request.method=='POST':
        marca=request.form['marca']
        modelo=request.form['modelo']
        precio=request.form['precio']
        ciudad=request.form['ciudad']

        cursor = mysql.connection.cursor()
        cursor.execute(" INSERT INTO coches VALUES(NULL,%s,%s,%s,%s)",
                        (marca,modelo,precio,ciudad)
        )
        # El commit guarda los cambios en la DB
        cursor.connection.commit()

        flash('Coche nuevo en Base de Datos!')
        return redirect(url_for ('index'))
    
    return render_template('crear_coche.html')


# Metodo para listar los coches.
@app.route('/coches')
def coches():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT * FROM coches')
    coches=cursor.fetchall()
    cursor.close()

    return render_template('coches.html', coches=coches)

# Metodo para listar un coche.
@app.route('/coche/<coche_id>')
def coche(coche_id):
    cursor=mysql.connection.cursor()
    cursor.execute("SELECT * FROM coches WHERE id = %s", (coche_id))
    coche=cursor.fetchall()
    cursor.close()

    return render_template('coche.html', coche=coche[0])




# Identifica que el nombre de la aplicacion de flask  sea de un proyecto de Flask.
if __name__ == '__main__':
    # Comprueba que funciona el srvidor correctamente y ademas cuando hacemos un cambio recarga y se reinicia automaticamente
    app.run(debug=True)