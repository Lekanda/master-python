
##### Redirecciones
-Primero crear la ruta en **urls.py**. Ponemos el tipo de dato y nombre     

```python
        path('pagina-pruebas/<int:redirigir>', miapp.views.pagina, name="pagina"),
```          

- Luego en **views.py**. 
```python
        # Importar de 'django.shortcuts'
        from django.shortcuts import render, HttpResponse, redirect

        # Poner en la funcion la redireccion
        def pagina(request,redirigir=0):
            if redirigir==1:
                return redirect('/contacto/Andres/Bernaola')
                # se puede poner una URL como google tmb

            return HttpResponse(layout+"""
                <h1>Pagina desde pagina de pruebas</h1>
            """)
```

---


### Plantillas y Templates en Django     


##### Templates Separadas           

- Creamos dentro de la carpeta de mi app (miapp) una carpeta llamada **templates**. _Dentro poner un archivo con el nombre de la funcion(index.html) y ahi pegamos el codigo HTML_.       

```html
        # index.html
        <h1>Hola Mundo con Django desde def index y html en template</h1>
        <p> Años hasta el 2050: </p>
```       

- En **settings.py**Añadir la app en _INSTALLED APPS_ para darla de alta

```python
        'miapp'
```       

- Para que la funcion(vista) devuelva la template poner en la vista.

```python
        # el render se importa arriba en views.py
        # render => renderiza la vista
        def index(request):
            return render(request,'index.html')

        #########################################

        #Otro ejemplo
        def hola_mundo(request):
            return render(request,'hola_mundo.html')
```      

> De esta forma es mas ordenado y facil de manejar las respuestas de las vistas, ademas, se trabaja en un archivo solo html.    


##### Layout, Bloques y Herencia de plantillas        

> Hasta ahora hemos utilizado los **layouts** de una forma simple.  

> Un bloque sustituye ese bloque por una template.
> Siempre hay que cerrarlos


- _Esta es la forma que se debe usar_ .Crear una template llamada **layout.html** y en ella:  
1. Crear funciones comunes en **layout.html** . En este caso  un _encabezado_, un _menu_  y un _footer_.
2. Crear un _bloque_  para el _titulo_.(_En esta caso se añade algo de txt despues_)
3. Crear _bloque_ de _contenido_ (**content**) dentro de un div
4. 

```python
            <!DOCTYPE html>
            <html lang="es">

            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>
                    {% block title %} 
                    {% endblock %} 
                    | Django
                </title>
            </head>

            <body>
                <h1>Sitio Web con Django</h1>
                <hr />
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
                    <li>
                        <a href="/contacto">Contacto</a>
                    </li>
                </ul>
                <hr/>

                <div id="content">
                    {% block content %}
                    {% endblock %}
                </div>

                <hr/>
                <footer>
                    Master en Python con Django &copy; Andres Bernaola
                </footer>    
            </body>
            </html>
```  
> Archivo **templates**/**layout.html**

- En cada template excepto el layout hay que configurarlas para que **hereden**  el _layout.html_.  
-Por ejemplo en template _pagina_, quedaria asi:
```py
        {% extends 'layout.html' %}

        {% block title %}
            Pagina de pruebas
        {% endblock %}

        {% block content %}
            <h1>Pagina desde pagina de pruebas</h1>
            <p>Hecho por Andres Bernaola</p>
        {% endblock %}
```  
> Se definen los dos bloques y hereda del _layout.html_

##### Herencia en Bloques y añadir contenido

- En el caso de querer poner en el div donde esta un bloque,  algo de codigo para que se ejecute siempre que se inserte cualquier bloque, ponemos esto.
```html
        {% block content %}
            {{block.super}}
            <h1>Pagina desde pagina de pruebas</h1>
            <p>Hecho por Andres Bernaola</p>
        {% endblock %}
```  
> {{block.super}} => coge del bloque padre lo que haya

##### Vincular CSS con Django  

- Crear dentro de la carpeta de la app(miapp), una carpeta _static_ y dentro 2 _carpetas_:
    -static
        - **css** => Aqui creamos un archivo **styles.css**
        - **images**  => para imagenes

- para poder utilizar hojas de estilos _CSS_ en _Django_:
- En _layout.html_:  
    - En parte superior cargamos los estaticos y debajo del titulo el link con CSS
```html
    {% load static %}
    <!DOCTYPE html>
```  

```html
    <link rel="stylesheet" type="text/css" href="{% static 'css/styles.css' %}"/>
```
> **static** => Le indicamos donde estan los estaticos. Esta incluida en Django. _No es el nombre de la carpeta_
> **css/styles.css** => La ruta dentro de la  carpeta _static_  

> **IMPORTANTE**: Es normal que no cargue el css si el serv esta en marcha. **REINICIAR EL SERVIDOR**  


---

### Estilos y Apariencia en Django

-El nombre un atributo _id_ en un _div_ se puede usar _solo_ una vez, es decir, en **id="x"** **x** solo se puede usar una vez  

> **.** => _clase_
> **#** => _id_

##### Estilos de Cabezera  

```css
/* El asterisco afecta a todos los elemnetos del DOM*/
*{}
```  

- Dar estilos desde _CSS_ :
```css
    /* ESTILOS GENERALES*/
    *{
        margin: 0px;
        padding: 0px;
        font-family: Arial, Helvetica, sans-serif;
        text-decoration: None; /* Quita los puntos de los enlaces*/
    }
    body{
        background-color: rgb(245, 245, 166);
    }
    /*Estilos Cabezera*/
    header{
        width: 1212px;
        height: 140px;
        background-color: rgb(213, 240, 117);
        margin: 0px auto;
    }
    #logotipo h1{
        display: block;
        letter-spacing: 2;
        text-transform: uppercase;
        font-weight: normal;
        color: #0b4e05;
    }
```  
>  Archivo static/css/*styles.css*  


##### Cargar Imagen en Template

- En *layout.html*,p ejem, poner:
``` html
    <img src="{% static 'images/logo.png' %}"/>
```  

- En *styles.css* ponemos estilos:
```css
    header{
    width: 1212px;
    height: 140px;
    background-color: rgb(213, 240, 117);
    margin: 0 auto;/* Centra el header*/
    }
    #logotipo{
        width: 37%;
        height: 140px;
        margin: 0 auto;/* Centra el logotipo*/
        padding-top: 1px;
    }
    #logotipo img{
        display: block;/*Deja manipular como quiera*/
        width: 72px;
        float: left;/*Para colocarlo a la izquierda*/
        margin-top: 32px;
    }
    #logotipo h1{
        display: block;/*Deja manipular como quiera*/
        float: left;
        margin-top: -72px;
        margin-left: 120px;
        letter-spacing: 2;
        font-weight: lighter;
        color: #0b4e05;
    }
```   
##### 198-199-200-201
- Estos capìtulos son de **CSS**  


---


### Lenguaje de plantillas y template tags en Django  

##### Comentarios en plantillas

- Para hacer un comentario en una plantilla  
```py
    {% comment 'Comentario sobre el codigo' %}
        <p>Esto tambien esta comentado</p>
    {% endcomment %}
```  

##### Pasar datos desde la vista y mostrarlos en la plantilla

- En views.py pasamos las variables al final de la funcion
```python
    return render(request,'index.html', {
        'title':'Home Page',
        'mi_variable':'Soy un dato que se pasa a la vista'
    })
```  
- En template index.html

```py
    {% block title %}
        {{title}}
    {% endblock %}
```   

##### Condicionales IF

- Asi se usan:
```html
    {% if nombre and nombre == 'Andres'%}
        <p>Mi nombre es : {{nombre}}</p>
    {% else %}
        <p>Mi nombre no existe cobarde</p>
    {% endif %}
```  

##### Condicionales FOR
- Ejemplo de un bucle FOR
```html
    <ul>
        {% for lenguaje in lenguajes %}
            <li>{{lenguaje}}</li>
        {% endfor %}
    </ul>
```   

##### Funcionalidades extra del bucle FOR

```html
<ul>
    {% for lenguaje in lenguajes %}
        <li>
            {{lenguaje}} 
            {{forloop.first}} => Da true en el primer elemento
            {{forloop.last}} => Da true en el ultimo elemento
            {{forloop.counter}} => Cuenta de elementos desde 1
            {{forloop.counter0}} => Cuenta de elementos desde 0
            {{forloop.revcounter}} => Cuenta de elementos desde 1 al reves
            {{forloop.revcounter0}} => Cuenta de elementos desde 0 al reves
        </li>
    {% empty %}
        <p>No hay lenguajes</p>
    {% endfor %}
</ul>
```   

##### El for montado en un archivo HTML

```html
<p> Años hasta el 2050:</p>
<ul>
    {{2021|divisibleby:2}}
    {% for year in years %}
        {% if year|divisibleby:2 == True %}
            <li>{{year}}</li>
        {% endif %}
    {% endfor %}
</ul>
```  

##### INCLUDES templates Django (Template en otra Template)  

- Se puede pasar una template en cualquier otra template
    - fecha-actual : Es otra *template*
    - Con *include* accedemos a la template *que esta en la misma carpeta*
```html
    {% include 'fecha-actual.html' %}
```  
> Los valores de la template de la template se heredan, es decir, los valores que tiene la template padre los tiene la hija tambien. -Cap:208   

- SE puede pasar valores a la template hija, que solo valen en esta. Pasamos valor *saludo* a la template hija desde la padre:   
```html
 {% include 'fecha-actual.html' with saludo="Hola Mundo desde plantilla" %}
```  
- Luego se pone en la template hija   
- Si añadimos **only** solo se pasan las hechas con *with*  
```html
 {% include 'fecha-actual.html' with saludo="Hola Mundo desde plantilla" only%}
```  

##### URLs en Templates  

- Cambiamos la configuracion del enlace en el menu de la barra de navegacion:  
```html
<li>
    <a href="{% url 'inicio' %}">Inicio</a>
</li>
```  
- ¿Que ganamos?:
    - Es mas practico y mejor para configurar
    - Enlaza con la etiqueta **name** en *urls.py*, no con la ruta
    - Si cambiamos la ruta del navegador en *urls.py* , se actualiza solo.  


##### Fechas en Templates  

- Tambien vale: h:m:s
```html
    {% now "d/m/Y" %}
```   
- Se pone donde se quiera en un htnml    



### Filtros en Templates  

##### Filtros por Defecto

- Pagina de documentacion:[https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#built-in-filter-reference](https://docs.djangoproject.com/en/3.1/ref/templates/builtins/#built-in-filter-reference)  
- Son *acciones predefinidas*, que nos permiten hacer acciones.  
- En este caso *nos quita los espacios* en una cadena de txt.
```html
    <p>{{"Hecho por Andres BernaolaOli"|cut:" "}}</p>
```   

- Sí pasamos una variable vacia, filtro para que haya un valor por defecto   
```html
        {{texto|default:"No hay nada"}}
```  
- Filtro para coger *primer* valor   
```html
        {{lista|first}}
```  
- Filtro para coger *ultimo* valor   
```html
        {{lista|last}}
```   
- Filtro para presentar *formateado*.
```html
        {{lista|join:', '}}
```   
- Filtro *devuelve tamaño* de lista.
```html
        {{lista|length}}
        {{"texto prueba"|length}}
```   
- Filtro convierte a *mayusculas*.
```html
        {{texto|upper}}
        {{"texto prueba"|upper}}
```   
- Filtro convierte a *minusculas*.
```html
        {{lista|lower}}
        {{"texto prueba"|length}}
```   
- Filtro devuelve un valor *aleatorio* de una *lista*.
```html
        {{lista|random}}
```   
- Filtro *limpia las etiquetas de HTML* y presenta en txt normal.
```html
        {{<h1>Hola</h1><p>Como estas</p><strong>Amigo mio</strong>|striptags}}
```   
- Se pueden *combinar varios filtros* a la vez. En este caso *cuenta el numero de palabras* despues de normalizar el txt con *striptags*
```html
        {{<h1>Hola</h1><p>Como estas</p><strong>Amigo mio</strong>|striptags|wordcount}}
```   

##### Filtros Personalizados


