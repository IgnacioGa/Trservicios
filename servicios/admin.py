from django.contrib import admin

from .models import Servicios, Imagenes, ImagenesPrincipales
# Register your models here.
class ImageArchive(admin.TabularInline):
    model = Imagenes
    extra = 3

class ImageAdmin(admin.ModelAdmin):
   inlines = [ImageArchive, ]


admin.site.register(Servicios, ImageAdmin)
admin.site.register(Imagenes)
admin.site.register(ImagenesPrincipales)