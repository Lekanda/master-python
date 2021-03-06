from django.contrib import admin
from .models import Category, Article


# Clase para ver las fechas de update y created
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('create_at',)
    search_fields=('name', 'descripcion')
    list_display=('name','description','create_at')
    ordering=('name',)
    

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=('user','create_at', 'updated_at',)
    search_fields=('title', 'content','user__username','categories__name')
    list_display=('title','public','user','create_at','updated_at','user_id')
    list_filter =('public','user__username','categories__name')
    # ordering=('public','user_username','categories__name')

    def save_model(self,request,obj,form,change):
        if not obj.user_id:
            obj.user_id=request.user.id
        obj.save()




# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
