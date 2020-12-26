from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def index(request):

    return render(request, 'mainapp/index.html', {
        'title':'Inicio'
    })


def about(request):

    return render(request, 'mainapp/about.html', {
        'title':'Sobre Nosotros'
    })


def register_page(request):
    
    register_form=RegisterForm()
    if request.method=='POST':
        register_form=RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Te has registrado correctamente!!')
            return redirect('inicio')


    return render(request, 'users/register.html',{
        'title':'Registro',
        'register_form':register_form
    })


def  login_page(request):

    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        #Funcion apara autenticar. Se pasan 3 cosas
        #    1. request
        #    2. username
        #    3. pass
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, 'Te has Logeado correctamente!!')
            return redirect('inicio')
        else:
            messages.warning(request, 'No estas logedado!!')
            return redirect('login')

    return render(request, 'users/login.html', {
        'title':'Identificate'
    })

