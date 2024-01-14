from django.db import models

# Create your models here.
class Service(models.Model):
    title=models.CharField(max_length=50, verbose_name='Servicio')
    content=models.TextField(verbose_name='Contenido')
    price=models.CharField(max_length=11, default='DESDE $', verbose_name='Precio')
    image=models.ImageField(upload_to='services', verbose_name='Imagen')
    created=models.DateTimeField(auto_now_add=True,  verbose_name= 'Fecha de creación')
    updated=models.DateTimeField(auto_now=True,  verbose_name= 'Fecha de edición')

    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'
        ordering=['created']
    
    def __str__(self):
        return self.title

class Testimony(models.Model):
    name=models.CharField(max_length=50, verbose_name='Nombre cliente')
    profession=models.CharField(max_length=50, verbose_name='Profesión')
    image=models.ImageField(upload_to='services', verbose_name='Imagen')
    testimony=models.TextField(verbose_name='Testimonio')
    service=models.ManyToManyField(Service, verbose_name='Servicio')
    created=models.DateTimeField(auto_now_add=True,  verbose_name= 'Fecha de creación')
    updated=models.DateTimeField(auto_now=True,  verbose_name= 'Fecha de edición')

    class Meta:
        verbose_name='testimonio'
        verbose_name_plural='testimonios'
        ordering=['created']
    
    def __str__(self):
        return self.name