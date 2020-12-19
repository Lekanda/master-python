from django.contrib import admin
from .models import Category, Article


# Clase para ver las fechas de update y created
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('create_at',)

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=('create_at', 'updated_at',)




# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
