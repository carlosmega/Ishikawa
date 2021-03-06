from django.db import models
from django.urls import reverse

from django.template.defaultfilters import slugify

# Create your models here.
class Hallazgo(models.Model):
    hallazgo = models.CharField(max_length=150)
    creado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hallazgo

    def get_absolute_url(self):
        return reverse('metodo:causas', kwargs={'pk': self.pk})

class Agrupador(models.Model):
    agrupador = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.agrupador

class Causa(models.Model):
    hallazgo = models.ForeignKey(Hallazgo, on_delete=models.CASCADE, blank=True, null=True)
    agrupador = models.ForeignKey(Agrupador, on_delete=models.CASCADE, blank=True, null=True)
    causa = models.CharField(max_length=350, blank=True, null=True)
    sev = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    det = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    occ = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    rpn = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    solucion = models.CharField(max_length=350, blank=True, null=True)
    responsable = models.CharField(max_length=350, blank=True, null=True)
    fecha_cierre = models.DateField(blank=True, null=True)
    comentarios = models.CharField(max_length=350, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.causa

    def save(self, *args, **kwargs):
        self.slug = slugify(self.causa)
        super(Causa, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('metodo:editar_causa', kwargs={'pk': self.hallazgo.pk, 'slug': self.slug})
        
    

        """
        if self.sev == 'NoneType' or self.det == 'NoneType' or self.occ == 'NoneType':
            print("ok")
        elif self.rpn != 'NoneType':
            self.rpn = self.sev * self.det * self.occ
            super(Causa, self).save()
        else:
        """
            
      
    

    



    
