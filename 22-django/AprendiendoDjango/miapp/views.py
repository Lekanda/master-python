from django.shortcuts import render, HttpResponse, redirect


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
    """
        
    year=2020
    while year<=2050:
        if year%2==0:
            html+=f"<li>{str(year)}</li>"
        year+=1

    html+="</ul>"

    return render(request,'index.html', {
        'title':'Home Page',
        'mi_variable':'Soy un dato que se pasa a la vista'
    })



def hola_mundo(request):
    return render(request,'hola_mundo.html')



def pagina(request,redirigir=0):
    # if redirigir==1:
    #     return redirect('/contacto/Andres/Bernaola')
        # se puede poner una URL como google tmb

    return render(request,'pagina.html')



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