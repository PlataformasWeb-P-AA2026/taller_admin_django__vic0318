from django.db import models

class Museo(models.Model):
    nombre = models.CharField(max_length=255, unique=True, verbose_name="Nombre")
    ciudad = models.CharField(max_length=150, verbose_name="Ciudad")
    anio_fundacion = models.IntegerField(verbose_name="Año de fundación")

    def __str__(self):
        return self.nombre

    @property
    def costo_total_produccion(self):
        total = self.guias.aggregate(total=models.Sum('exhibiciones__costo_produccion'))['total']
        return total or 0.0

    @property
    def guias_mas_experimentados(self):
        max_exp = self.guias.aggregate(max_exp=models.Max('anios_experiencia_guia'))['max_exp']
        if max_exp is None:
            return "Sin guías"
        guias_top = self.guias.filter(anios_experiencia_guia=max_exp)
        nombres = [g.nombre_completo for g in guias_top]
        return ", ".join(nombres)

    class Meta:
        verbose_name = "Museo"
        verbose_name_plural = "Museos"


class GuiaMuseo(models.Model):
    nombre_completo = models.CharField(max_length=255, verbose_name="Nombre completo")
    anios_experiencia_guia = models.IntegerField(verbose_name="Años de experiencia")
    idiomas_hablados = models.CharField(max_length=255, verbose_name="Idiomas hablados")
    museo = models.ForeignKey(Museo, on_delete=models.CASCADE, related_name="guias", verbose_name="Museo")

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name = "Guía de Museo"
        verbose_name_plural = "Guías de Museo"


class Exhibicion(models.Model):
    titulo_exhibicion = models.CharField(max_length=255, verbose_name="Título de la exhibición")
    duracion_meses = models.IntegerField(verbose_name="Duración (meses)")
    costo_produccion = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Costo de producción")
    tematica = models.CharField(max_length=255, verbose_name="Temática")
    guia = models.ForeignKey(GuiaMuseo, on_delete=models.CASCADE, related_name="exhibiciones", verbose_name="Guía de museo")

    def __str__(self):
        return self.titulo_exhibicion

    class Meta:
        verbose_name = "Exhibición"
        verbose_name_plural = "Exhibiciones"
