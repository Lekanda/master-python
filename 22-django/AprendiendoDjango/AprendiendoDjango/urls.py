"""AprendiendoDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#importar app con mis vistas
# from miapp import views
import miapp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', miapp.views.index, name="index"),
    path('inicio/', miapp.views.index, name="inicio"),
    path('contacto/<str:nombre>', miapp.views.contacto, name="contacto"),
    path('pagina-pruebas/', miapp.views.pagina, name="pagina"),
    path('hola-mundo/', miapp.views.hola_mundo, name="hola_mundo")
]
