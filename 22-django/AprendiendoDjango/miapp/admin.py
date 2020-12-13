from django.contrib import admin
from .models import Article, Category

# Register your models here.
# Al registrarlos crea un CRUD de los datos en el Admin Panel
admin.site.register(Article)
admin.site.register(Category)
