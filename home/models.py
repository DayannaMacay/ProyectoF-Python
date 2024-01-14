from django.db import models

# Create your models here.
class Home(models.Model):
    slogan=models.CharField(max_length=50, verbose_name='Eslogan')
    image=models.ImageField(upload_to='home', verbose_name='Imagen')
    location = models.CharField(max_length=250, default='AV. 6 DE DICIEMBRE - LA NIÑA', verbose_name='Dirección')
    phone = models.CharField(max_length=15, default='+593 94 534 5446', verbose_name='Teléfono  ')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name='home'
        verbose_name_plural='home'
        ordering=['created']

    def __str__(self):
        return self.slogan