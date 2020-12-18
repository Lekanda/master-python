from pages.models import Page

def get_pages(request):
    
    # Trae todos , pero solo el primer campo
    # pages=Page.objects.all()

    # trae de la DB estos valores solo
    pages=Page.objects.values_list('id', 'title', 'slug')

    # flat=True => texto plano
    # pages=Page.objects.values_list('title', flat=True)

    return {
        'pages':pages
    }

    