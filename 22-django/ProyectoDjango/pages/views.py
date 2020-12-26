from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login") # Decorador: Login requerido
def page(request,slug):
    #
    page= Page.objects.get(slug=slug)
    # slug=slug => nombre del campo; valor que se pasa en la url


    return render(request, "pages/page.html",{
        "page":page
    })

