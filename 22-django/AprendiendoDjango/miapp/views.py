from django.shortcuts import render, HttpResponse


# Create your views here.
# MVC => Modelo, Vista , Controlador
# MTV => Modelo, Template , Vista

def hola_mundo(request):
    return HttpResponse(
    """
            <h1>Hola Mundo con Django</h1>
            <p> Esta es una prueba de triple comilla</p>
            <label>Etiqueta de campo</label>
            <input type="text"/>
    """
    )