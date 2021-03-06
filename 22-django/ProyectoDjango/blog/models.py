from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100, verbose_name='Nombre')
    description=models.CharField(max_length=255,verbose_name='Descripcion')
    create_at=models.DateTimeField(auto_now_add=True, verbose_name='Creado el')

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
    # Metodo Magico
    def __str__(self):
        # al crear la categoria imprime el return(nombre de categoria)
        return self.name


class Article(models.Model):
    title=models.CharField(max_length=150,verbose_name='Titulo')
    content=RichTextField(verbose_name='Contenido')
    image=models.ImageField(default='null', verbose_name='Imagen', upload_to="articles")
    public=models.BooleanField(verbose_name='¿Publicado?')
    # Relacion de cada articulo tiene un usuario
    user=models.ForeignKey(User, editable=False,verbose_name='Usuario', on_delete=models.CASCADE)
    # Relacion muchos a muchos: Un ariculo tiene muchas categorias. una categoria puede estar en muchos articulos
    # blank=True => No es obligatorio
    categories= models.ManyToManyField(Category, verbose_name='Categorias', blank=True, related_name="articles")
    create_at=models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at=models.DateTimeField(auto_now=True, verbose_name='Actualizado el')

    class Meta:
        verbose_name='Articulo'
        verbose_name_plural='Articulos'
        ordering=['-create_at']
    # Metodo Magico
    def __str__(self):
        # al crear la categoria imprime el return(titulo de articulo)
        return self.title
