# ![Django](imagenes/django.ico) Framework de Python

---

### Instalacion de Django
- En web de [Django](https://www.djangoproject.com/download/) copiar link: `pip install Django==3.1.4``

- **django-admin startproject 'nombreProyecto'** => Inicia el proyecto Django (NO METER GUIONES en _nombreProyecto_)(En la carpeta de proyecto).
    - Link a [Documentacion](https://docs.djangoproject.com/en/3.1/intro/tutorial01/#creating-a-project)

- **manage.py** => es una consola. si ponemos:
```console
        python manage.py help
```
> Nos da los comandos disponibles para la consola
> CUIDADO CON LA UBICACION. Crea 2 carpetas. Asegurar que se esta en la carpeta adecuada


### Migrar el Proyecto
- Nos crea la estructura para  DB, de SQLite:
```console
        python manage.py migrate
```

### Arrancar el servidor
- Ejecutar en consola y en carpeta de proyecto _F:\Mis Documentos\Mis Cursos\Python\master-python\22-django\AprendiendoDjango>_.p ejm
```console
        python manage.py runserver
```


---


### Crear APPs en Django
- Un a App en el fondo es un paquete de Python. Crea funcionalidades. Por ejemplo la de admin
- Se puede tener apps para cualquier  parte logica, funciones , etc.. de la app
- Para crear la APP. En carpeta _F:\Mis Documentos\Mis Cursos\Python\master-python\22-django\AprendiendoDjango>_:
```console
        python manage.py startapp nombreApp
```
> Esto crea la APP
- A la hora de poner los nombre a las apps que sean logicos


---


### Vistas & Rutas
- Estas configuraciones se hacen desde el archivo **views.py**

- Estas son las diferencias en la arquitectura.    

1. **MVC** => Modelo, **Vista** , **Controlador** => En JS y otros     

2. **MTV** => Modelo, **Template** , **Vista** => En Python    

> Fijarse que cambian los nombres CUIDADO. Los nombres estan ordenados

##### Vistas
- Las vistas son en MVT como el controlador en MVC.
- Para crear una vista , en **views.py** en App _miapp_ :
```python
            def hola_mundo(request):
                return HttpResponse(
                """
                    <h1>Hola Mundo con Django</h1>
                    <p> Esta es una prueba de triple comilla</p>
                    <label>Etiqueta de campo</label>
                    <input type="text"/>
                """
                )
```
##### Crear una ruta 
-En App principal del proyecto en **urls.py** configurarlo asi:
```python
    path('hola-mundo/', views.hola_mundo, name="hola_mundo")
]
```
- `'hola-mundo/'` => la ruta para el nav
- `views.hola_mundo` => la funcion que hace , esta en **views.py**. Hay que importarla con `from miapp import views`.
- `name="hola_mundo"` => nombre de la ruta

> **HttpResponse** => nos permite meter datos al DOM mediante HTML

##### Multiples vistas y urls
- Para crear la pantalla pral(_index.html_):
```python
            path('', views.index, name="index"),
```   

- Para crear una vista que sirva para otras se puede hacer con :
```python
            path('inicio/', views.index, name="inicio"),
```    

> **Para importar dede una APP es mejor el metodo**     

```python
            import miapp.views
            # Cuando hay muchas Apps y metodos es mejor asi, mas visual
```    
- Otra forma de usar una funcion en **views**
- Se Puede hacer cualquier operacion       

```python
        def index(request):
            html= """
                <h1>Hola Mundo con Django desde def index</h1>
                <p> Años hasta el 2050: </p>
                <ul>
            """
            year=2020
            while year<=2050:
                if year%2==0:
                    html+=f"<li>{str(year)}</li>"
                year+=1

            html+="</ul>"

            return HttpResponse(html)
```    

##### Navegacion entre rutas(LAYOUT)
- Para crear un **layout** creamos y concatenamos a la respuesta de la funcion. P Ejem
```python
        # Crear LAYOUT
        layout= """
            <h1>Sitio Web con Django</h1>
                <hr/>
                <ul>
                    <li>
                        <a href="/inicio">Inicio</a>
                    </li>
                    <li>
                        <a href="/hola-mundo">Hola Mundo</a>
                    </li>
                    <li>
                        <a href="/pagina-pruebas">Pagina</a>
                    </li>

                </ul>
        """

        # Concatenar la respuesta
        def pagina_pruebas(request):
            return HttpResponse(layout+"""
            <h1>Pagina desde pagina de pruebas</h1>
            """)
```
> Esto nos da com resultado un Layout en cualquier sitio que se ponga     

##### Parametros entre Rutas
- Se trata de poder mandar argumentos a un metodo de una vista.
- En **urls.py** ponemos y pasmos el parametro asi:
```python
     path('contacto/<str:nombre>', miapp.views.contacto, name="contacto"),
```    
- En la funcion pasamos los argumentos:
```python
    def contacto(request,nombre):
        return HttpResponse(layout + f"""
            <h1>Contacto {nombre}</h1>
        """)
```     
- A la hora de llamar a la funcion lo haremos asi:
        `http://127.0.0.1:8000/contacto/Andres`
> la ruta ahora necesita un parametro en la URL    

- Se pueden pasar mas de 1 parametro. Cuuidado con el orden       


##### Parametros Opcionales
- Se puede hacer que los parametros no sean obligatorios como en el ejemplo anterior(Parametros entre Rutas).
- Hay que definir en las rutas todos los casos posibles en 
```python
    # En urls.py
    path('contacto/', miapp.views.contacto, name="contacto"),
    path('contacto/<str:nombre>/', miapp.views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellidos>', miapp.views.contacto, name="contacto"),
```     
- Una opcion para cada caso, no es necesario tener todas, solo las necesarias     
```python
    # en views.py
    def contacto(request,nombre="",apellidos=""):
    html=""
    if nombre and apellidos:
        html+= "<p>El nombre completo es :</p>"
        html+=f"<h3>{nombre} {apellidos}</h3>"
    elif nombre:
        html+= "<p>El nombre es :</p>"
        html+=f"<h3>{nombre}</h3>"
    elif  nombre!=True and apellidos!=True:
        html+= "<p>No hay datos :</p>"

    return HttpResponse(layout+f"""
            <h1>Contacto </h1>
    """ + html)
```

