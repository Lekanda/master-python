from django.shortcuts import render,get_object_or_404
# Importar los modelos
from blog.models import Category, Article

# Create your views here.

def list(request):

    articles=Article.objects.all()

    return render(request, 'articles/list.html',{
        'title':'Articulos',
        'articles':articles
    })

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
    

# category = get_object_or_404(Category,id=category_id)