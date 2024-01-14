from django.db import models

# Create your models here.
class Schedule(models.Model): # Schedule = Horario
    days=models.CharField(max_length=10, verbose_name='Día')
    hours=models.CharField(max_length=15, default='09 AM - 09 PM', verbose_name='Horas')
    created=models.DateTimeField(auto_now_add=True,  verbose_name= 'Fecha de creación')
    updated=models.DateTimeField(auto_now=True,  verbose_name= 'Fecha de edición')

    class Meta:
        verbose_name='horario'
        verbose_name_plural='horarios'
        ordering=['created']
    
    def __str__(self):
        return self.days

class About(models.Model):
    name=models.CharField(max_length=50, verbose_name='Nombre')
    profession=models.CharField(max_length=50, verbose_name='Profesión')
    image=models.ImageField(upload_to='about', verbose_name='Imagen')
    schedules=models.ManyToManyField(Schedule, verbose_name='Horarios')
    created=models.DateTimeField(auto_now_add=True,  verbose_name= 'Fecha de creación')
    updated=models.DateTimeField(auto_now=True,  verbose_name= 'Fecha de edición')

    class Meta:
        verbose_name='barbero'
        verbose_name_plural='barberos'
        ordering=['created']

    def __str__(self):
        return self.name