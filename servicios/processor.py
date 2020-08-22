from .models import Servicios

def foos(request):
    return {'servi': Servicios.objects.all()}