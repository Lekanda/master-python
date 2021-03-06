from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator
# Importar los modelos
from blog.models import Category, Article
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login") # Decorador: Login 
def list(request):
    # Sacar Articulos
    articles=Article.objects.all()
    # Paginar Articulos
    paginator = Paginator(articles, 2)
    # Recoger el numero pagina
    page=request.GET.get('page')
    page_articles=paginator.get_page(page)


    return render(request, 'articles/list.html',{
        'title':'Articulos',
        'articles':page_articles
    })

@login_required(login_url="login") # Decorador: Login 
def category(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        # articles= Article.objects.filter(categories=category_id)

        return render(request, 'categories/category.html', {
        'category': category
        # 'articles': articles
    })
    except Category.DoesNotExist:
        return render(request,'errores/404.html')
 

@login_required(login_url="login") # Decorador: Login 
def article(request, article_id):

    try:
        article = Article.objects.get(id=article_id)

        return render(request, 'articles/detail.html', {
        'article': article
    })
    except Article.DoesNotExist:
        return render(request,'errores/404.html')