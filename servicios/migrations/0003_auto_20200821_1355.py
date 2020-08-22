# Generated by Django 3.0.8 on 2020-08-21 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_imagenes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagenes',
            name='imgprincipal',
        ),
        migrations.AddField(
            model_name='servicios',
            name='imgprincipal',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Principal'),
        ),
    ]