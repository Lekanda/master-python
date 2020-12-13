from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
from django.db.models import Q
from miapp.forms import FormArticle


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



###############################
# Crear Articulo mediante URL
###############################
# Crear articulo mediante la URL
def crear_articulo(request,title,content,public):
    articulo=Article(
        title = title,
        content = content,
        public = public
    )
    articulo.save()

    return HttpResponse(f"Articulo Creado: <strong>{articulo.title} - {articulo.content}</strong> ")


# Crear articulo 
def save_article(request):
    if request.method == 'POST':
        title = request.POST['title']
        if len(title)<=5 :
            return HttpResponse("<h2>El titulo es muy pequeño</h2>")

        content= request.POST['content']
        public= request.POST['public']


        articulo=Article(
        title = title,
        content = content,
        public = public
        )
        articulo.save()
        return HttpResponse(f"Articulo Creado: <strong>{articulo.title} - {articulo.content}</strong>")
    else:
        return HttpResponse("<h2>No se creo el articulo</h2>")

def create_article(request):
    return render(request,'create_article.html')

def create_full_article(request):
    if request.method == 'POST':
        formulario = FormArticle(request.POST)

        if formulario.is_valid():
            data_form=formulario.cleaned_data
            title=data_form.get('title')
            content=data_form['content']
            public=data_form['public']

            articulo=Article(
                title = title,
                content = content,
                public = public
            )
        articulo.save()
        return redirect('articulos')
        # return HttpResponse(articulo.title + ' - ' + articulo.content + ' - ' + str(articulo.public))
    else:
        formulario = FormArticle()



    formulario=FormArticle()
    return render(request, 'create_full_article.html' ,{
        'form': formulario
    })






######################################################
####################FIN##############################
#######################################################




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
# Lista todos los registros de la tabla.
def articulos(request):
    articulos=Article.objects.all().order_by('-id')
    # .all=>Saca  todos los registros de la DB
    # Tiene menos opciones que get()
    return render(request, 'articulos.html', {
        'articulos':articulos
    })


##################################
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


##################################
# FILTER => Obtiene un registro por title en este caso
# Se pueden poner mas condiciones: (title="Caza menor",id=8)
# def articulos(request):
#     # lookups => da opciones para buscar en los campos.
#     # (title__contains="articulo") => Sí en title contiene 'articulo'
#     # (title__exact="articulo") => Sí en title titulo exacto 'articulo'
#     # (title__iexact="articulo") => Sí en title titulo exacto 'articulo' sin mirar Mayus o Minus
#     articulos=Article.objects.filter(title__contains="articulo")
#     return render(request, 'articulos.html', {
#         'articulos':articulos
#     })


#######################
# Buscar por aquellos que tengan un id mayor que 15
# def articulos(request):
#     articulos=Article.objects.filter(id__gt=15)
#     # filter(id__gt=12) => id 'mas grande que' (great than)
#     # filter(id__gte=12) => id 'igual o mas grande que'
#     # filter(id__lt=12) => id 'mas pequeño que' (less than)
#     # filter(id__lte=12) => id 'igual o mas pequeño que'
#     # filter(id__lte=12, title__contains="articulo") => id 'igual o mas pequeño que' y titulo 'igual a'. 2 Condiciones
#     return render(request, 'articulos.html', {
#         'articulos':articulos
#     })


######################
# EXCLUDE => Excluye segun la condicion.
# def articulos(request):
#     articulos=Article.objects.filter(
#         title="Articulo"
#     ).exclude(public=False)

#     articulos=Article.objects.raw("SELECT * FROM miapp_article WHERE title='Articulo' AND public=0")
#     return render(request, 'articulos.html', {
#         'articulos':articulos
#     })


#################
# OR en consulta a ORM.
# def articulos(request):
#     articulos=Article.objects.filter(
#         # Que el title contenga 2 'o' 3 en su txt.
#         Q(title__contains="2") | Q(title__contains="3")
#     )
#     return render(request, 'articulos.html', {
#         'articulos':articulos
#     })
#######################################################
#################### FIN ##############################
#######################################################


# Borrar un Registro
def borrar_articulo(request,id):
    articulo=Article.objects.get(pk=id)
    articulo.delete()
    return redirect('articulos')