# Generated by Django 5.0.1 on 2024-01-13 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='phone',
            field=models.TextField(default='+593 94 534 5446', verbose_name='Teléfono  '),
        ),
    ]
