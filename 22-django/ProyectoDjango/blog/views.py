from django.shortcuts import render
# Importar los modelos
from blog.models import Category, Article

# Create your views here.

def list(request):

    articles=Article.objects.all()

    return render(request, 'articles/list.html',{
        'title':'Articulos',
        'articles':articles
    })