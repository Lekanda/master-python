from django.contrib import admin
from .models import Page


# Configuracion extra para el modelo
class PageAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at')
    search_fields=('title', 'content')
    list_filter=('visible',)
    list_display=('title','order','slug','visible','created_at','updated_at')
    ordering=('order',)

# Register your models here.
admin.site.register(Page,PageAdmin)


############ Configuracion del Admin Panel ############
title="Proyecto 2 Django"
subtitle="Panel de gestion"
# Cabecera del AdPan
admin.site.site_header = title
# Pestaña del AdPan
admin.site.site_title = title
# Subtitulo dela Adpan
admin.site.index_title = subtitle

