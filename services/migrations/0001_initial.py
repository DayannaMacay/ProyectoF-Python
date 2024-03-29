# Generated by Django 5.0.1 on 2024-01-14 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Servicio')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('price', models.CharField(default='DESDE $', max_length=11, verbose_name='Precio')),
                ('image', models.ImageField(upload_to='services', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'servicio',
                'verbose_name_plural': 'servicios',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre cliente')),
                ('profession', models.CharField(max_length=50, verbose_name='Profesión')),
                ('image', models.ImageField(upload_to='services', verbose_name='Imagen')),
                ('testimony', models.CharField(max_length=50, verbose_name='Testimonio')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('service', models.ManyToManyField(to='services.service', verbose_name='Servicio')),
            ],
            options={
                'verbose_name': 'testimonio',
                'verbose_name_plural': 'testimonios',
                'ordering': ['created'],
            },
        ),
    ]
