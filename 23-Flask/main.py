# Importar Flask
from flask import Flask

# Crear la app general de Flask
app=Flask(__name__)

# Crear ruta
@app.route('/')
def index():
    return "Aprendiendo FLASK"

# Identifica que el nombre de la aplicacion de flask  sea de un proyecto de Flask.
if __name__ == '__main__':
    # Comprueba que funciona el srvidor correctamente y ademas cuando hacemos un cambio recarga y se reinicia automaticamente
    app.run(debug=True)