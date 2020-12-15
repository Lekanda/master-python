from django.contrib import admin
from .models import Article, Category

# Register your models here.
# Clase para crear en AdminPanel campos de solo lectura. P ejm: campo de fecha de creacion 
class  ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
# Al registrarlos crea un CRUD de los datos en el Admin Panel
admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)



title="Administracion de Gestor de Articulos 5"
# Configurar cabecera del AdminPanel
admin.site.site_header=title
# Configurar el titulo del AdminPanel
admin.site.site_title=title
# Configura  el nombre de la pestaña  y subtitulo
admin.site.index_title="Panel de Admin"


