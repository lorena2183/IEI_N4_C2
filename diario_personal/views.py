from django.shortcuts import render
from rest_framework import viewsets

from .models import Usuario
from .models import Categoria
from .models import Etiqueta
from .models import EntradaDiario
from .models import HistorialEntrada

from .serializer import UsuarioSerializer
from .serializer import CategoriaSerializer
from .serializer import EtiquetaSerializer
from .serializer import EntradaDiarioSerializer
from .serializer import HistorialEntradaSerializer

# Create your views here.
def inicio(request):
    return render(request,'diario_personal/inicio.html')

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer

class EntradaDiarioViewSet(viewsets.ModelViewSet):
    queryset = EntradaDiario.objects.all()
    serializer_class = EntradaDiarioSerializer

class HistorialEntradaViewSet(viewsets.ModelViewSet):
    queryset = HistorialEntrada.objects.all()
    serializer_class = HistorialEntradaSerializer
