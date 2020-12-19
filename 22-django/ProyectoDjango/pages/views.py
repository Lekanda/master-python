from django.shortcuts import render
from .models import Page

# Create your views here.

def page(request,slug):
    #
    page= Page.objects.get(slug=slug)
    # slug=slug => nombre del campo; valor que se pasa en la url


    return render(request, "pages/page.html",{
        "page":page
    })

