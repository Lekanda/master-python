from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article


# Create your views here.
# MVC => Modelo, Vista , Controlador
# MTV => Modelo, Template , Vista

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
        <li>
            <a href="/contacto">Contacto</a>
        </li>
    </ul>
    <hr/>
"""



def index(request):

    year=2021
    hasta=range(year,2051)


    nombre='Andres'
    lenguajes=['JavaScript','Python','HTML','C','Java','C#']
    # lenguajes=[]

    return render(request,'index.html', {
        'title':'Home Page',
        'mi_variable':'Soy un dato que se pasa a la vista',
        'nombre':nombre,
        'lenguajes':lenguajes,
        'years':hasta
    })



def hola_mundo(request):
    return render(request,'hola_mundo.html')



def pagina(request,redirigir=0):
    # if redirigir==1:
    #     return redirect('/contacto/Andres/Bernaola')
        # se puede poner una URL como google tmb

    return render(request,'pagina.html', {
        'texto':'Texto desde views',
        'lista':['uno','dos','tres','cuatro','cinco']
    })



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
    """+html)



def crear_articulo(request,title,content,public):
    articulo=Article(
        title = title,
        content = content,
        public = public
    )
    articulo.save()

    return HttpResponse(f"Articulo Creado: {articulo.title} - {articulo.content} ")