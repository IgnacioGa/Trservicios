from django.db import models

# Create your models here.
class Servicios(models.Model):
	servicio = models.CharField(max_length=64)
	descripcion = models.TextField()
	imgprincipal = models.ImageField(upload_to='galeria', verbose_name='Principal', default='gallery/static/images/no-img.jpg')

	def __str__(self):
		return f"{self.id}:{self.servicio}"

class ImagenesPrincipales(models.Model):
	principal = models.ImageField(upload_to='inicio', verbose_name='Principal', default='gallery/static/images/no-img.jpg')
	descripcion = models.TextField()
	referencia = models.ForeignKey(Servicios, on_delete=models.CASCADE, related_name="inicioServicio")

	def __str__(self):
		return f"{self.principal} hace referencia a {self.referencia}"

class Imagenes(models.Model):	
	imagen = models.ImageField(upload_to='images', verbose_name='Imagenes')
	servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE, related_name="imgServicio")
	descripcion = models.TextField(blank = True, null=True)

	def __str__(self):
		return f"Imagenes de este servicio= {self.servicio}"
		