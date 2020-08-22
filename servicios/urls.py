from django.urls import path


from . import views

app_name = "sev"
urlpatterns = [
    path("", views.index, name="index"),
    path("servicio/<str:servicio>", views.servicio, name="servicio"),
]
