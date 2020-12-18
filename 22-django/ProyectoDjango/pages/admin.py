from django.contrib import admin
from .models import Page

# Register your models here.
admin.site.register(Page)


############ Configuracion del Admin Panel ############
title="Proyecto 2 Django"
subtitle="Panel de gestion"
# Cabecera del AdPan
admin.site.site_header = title
# Pestaña del AdPan
admin.site.site_title = title
# Subtitulo dela Adpan
admin.site.index_title = subtitle

