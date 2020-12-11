from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article


# Create your views here.
# MVC => Modelo, Vista , Controlador
# MTV => Modelo, Template , Vista

# LAYOUT
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

# Index principal
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

# Funcion HolaMundo
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

# Crear contacto 
def contacto(request,nombre="",apellidos=""):
    return render(request,'contacto.html', {
        'nombre':nombre,
        'apellidos':apellidos
    })

# Crear Articulo mediante URL
def crear_articulo(request,title,content,public):
    articulo=Article(
        title = title,
        content = content,
        public = public
    )
    articulo.save()

    return HttpResponse(f"Articulo Creado: {articulo.title} - {articulo.content} ")

# Buscar articulo por PrimaryKey(7) y sí es public=False
def articulo(request):
    try:
        articulo=Article.objects.get(pk=7,public=False)
        # Funciona igual con: id, title, content que con pk
        # public=True => Segundo argumento para la busqueda de un registro
        response = f"Articulo: {articulo.title}"
    except:
        response = "<h1> Articulo no encontrado</h1>"

    return HttpResponse(response)

# Editar registro
def editar_articulo(request, id):
    articulo=Article.objects.get(pk=id)

    articulo.title = "batman en japon"
    articulo.content = "Pelicula edl 2017"
    articulo.public = True


    articulo.save()

    return HttpResponse(f"Articulo editado: {articulo.title} - {articulo.content} ")

######################################################
########Lista todos los registros de la DB############
######################################################
# Lista todos los que hay
def articulos(request):
    articulos=Article.objects.all()
    # .all=>Saca  todos los registros de la DB
    # Tiene menos opciones que get()
    return render(request, 'articulos.html', {
        'articulos':articulos
    })
# Lista y ordena registros por 'title' y los limita a 3 registros
# def articulos(request):
#     articulos=Article.objects.order_by('title')[1:3]
#     # order_by => ordenar por:
#     #   title => por titulo
#     #   id => por id
#     #   -id => por id al reves
#     ##########################
#     # [:3] => Limita a 3 los registros que se cogen.
#     # [3:7] => Limita a  registros del 3 al 7 ,que se han cogido.
#     return render(request, 'articulos.html', {
#         'articulos':articulos
#     })
######################################################

# Borrar un Registro
def borrar_articulo(request,id):
    articulo=Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')