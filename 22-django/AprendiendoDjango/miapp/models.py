from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Miniatura")
    public = models.BooleanField(verbose_name="¿Publicado?")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Nombre singular
        verbose_name = "Articulo"
        # Nombre plural
        verbose_name_plural = "Articulos"
        # Orden x 'propiedad'
        ordering = ['public']



class Category(models.Model):
    name = models.CharField(max_length=110)
    description= models.CharField(max_length=250)
    created_at= models.DateField()

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

