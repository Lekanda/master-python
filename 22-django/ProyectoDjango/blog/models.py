from django.db import models

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