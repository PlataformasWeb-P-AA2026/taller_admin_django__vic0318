from django.contrib import admin
from .models import Museo, GuiaMuseo, Exhibicion

@admin.register(Museo)
class MuseoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ciudad', 'anio_fundacion', 'costo_total_produccion_display', 'guias_mas_experimentados_display')
    search_fields = ('nombre', 'ciudad')
    list_filter = ('ciudad', 'anio_fundacion')
    ordering = ('nombre',)

    def costo_total_produccion_display(self, obj):
        return f"${obj.costo_total_produccion:,.2f}"
    costo_total_produccion_display.short_description = "Costo Total Producción"

    def guias_mas_experimentados_display(self, obj):
        return obj.guias_mas_experimentados
    guias_mas_experimentados_display.short_description = "Guía(s) con más experiencia"

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
