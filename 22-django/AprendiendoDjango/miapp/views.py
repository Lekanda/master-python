from django.shortcuts import render, HttpResponse


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

    return HttpResponse(layout+html)

def hola_mundo(request):
    return HttpResponse(layout+"""
            <h1>Hola Mundo con Django</h1>
            <p> Esta es una prueba de triple comilla</p>
            <label>Etiqueta de campo</label>
            <input type="text"/>
    """)

def pagina(request):
    return HttpResponse(layout+"""
            <h1>Pagina desde pagina de pruebas</h1>
    """)

def contacto(request,nombre):
    return HttpResponse(layout+f"""
            <h1>Contacto {nombre}</h1>
    """)