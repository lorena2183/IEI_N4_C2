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
    # ---- Páginas web (listas) ----
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('etiquetas/', views.lista_etiquetas, name='lista_etiquetas'),
    path('entradas/', views.lista_entradas, name='entradas'),
    path('entradas/nueva/', views.crear_entrada, name='nueva_entrada'),
    path('historial/', views.lista_historial, name='lista_historial'),
    path('salir/', views.salir, name='salir'),

    # ---- API (DRF) ----
    path('', include(enrutador.urls)),
]
