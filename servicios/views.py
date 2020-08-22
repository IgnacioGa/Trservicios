from django.shortcuts import render

from .models import Servicios, Imagenes, ImagenesPrincipales

from .forms import Consulta

# Create your views here.
def index(request):
	return render(request, "servicios/index.html",{
		"servicio": Servicios.objects.all(),
		"banner": ImagenesPrincipales.objects.all(),
		})

def servicio(request, servicio):
	form = Consulta()
	servicioSeleccionado = Servicios.objects.filter(servicio=servicio)
	lisImagenes = Imagenes.objects.filter(servicio__in=servicioSeleccionado).all()
	return render(request, "servicios/servicio.html",{
		"servicio": servicioSeleccionado,
		"img": lisImagenes,
		"form": form
		})