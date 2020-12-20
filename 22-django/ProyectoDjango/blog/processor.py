from blog.models import Category

def get_categories(request):
    

    # trae de la DB estos valores solo
    categories=Category.objects.values_list('id', 'name')

    return {
        'categories':categories
    }