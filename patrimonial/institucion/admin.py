from django.contrib import admin
from .models import Museo, GuiaMuseo, Exhibicion

@admin.register(Museo)
class MuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'anio_fundacion')
    search_fields = ('nombre', 'ciudad')
    list_filter = ('ciudad', 'anio_fundacion')
    ordering = ('nombre',)

@admin.register(GuiaMuseo)
class GuiaMuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'anios_experiencia_guia', 'idiomas_hablados', 'museo')
    search_fields = ('nombre_completo', 'idiomas_hablados')
    list_filter = ('museo', 'anios_experiencia_guia')
    ordering = ('nombre_completo',)

@admin.register(Exhibicion)
class ExhibicionAdmin(admin.ModelAdmin):
    list_display = ('titulo_exhibicion', 'duracion_meses', 'costo_produccion', 'tematica', 'guia')
    search_fields = ('titulo_exhibicion', 'tematica')
    list_filter = ('guia', 'tematica', 'duracion_meses')
    ordering = ('titulo_exhibicion',)
