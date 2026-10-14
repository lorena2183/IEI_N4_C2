from django.urls import path
from . import views

from django.urls import path, include
from rest_framework import routers
from diario_personal import views

enrutador = routers.DefaultRouter()

enrutador.register(r'Usuario', views.UsuarioViewSet)
enrutador.register(r'Categoria', views.CategoriaViewSet)
enrutador.register(r'Etiqueta', views.EtiquetaViewSet)
enrutador.register(r'EntradaDiario', views.EntradaDiarioViewSet)
enrutador.register(r'HistorialEntrada', views.HistorialEntradaViewSet)


urlpatterns = [
    path('', include(enrutador.urls))
]


