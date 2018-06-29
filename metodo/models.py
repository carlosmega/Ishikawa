from django.db import models

from django.urls import reverse

# Create your models here.
class Hallazgo(models.Model):
    hallazgo = models.CharField(max_length=150)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hallazgo

    def get_absolute_url(self):
        return reverse('metodo:causas', kwargs={'pk': self.pk})

class Causa(models.Model):
    hallazgo = models.ForeignKey(Hallazgo, on_delete=models.CASCADE, blank=True, null=True)
    causa = models.CharField(max_length=350, blank=True, null=True)
    sev = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    det = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    occ = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    rpn = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    solucion = models.CharField(max_length=350, blank=True, null=True)
    responsable = models.CharField(max_length=350, blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)
    comentarios = models.CharField(max_length=350, blank=True, null=True)

    def __str__(self):
        return self.causa

    def save(self):
        self.rpn = self.sev * self.det * self.occ
        super(Causa, self).save()


    



    
