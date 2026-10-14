from rest_framework import serializers

from .models import Usuario
from .models import Categoria
from .models import Etiqueta
from .models import EntradaDiario
from .models import HistorialEntrada

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fileds = ('nombre_usuario','email','contrasena','fecha_nacimiento')
        # __all__ serializa todas los atributos de la clase/modelo

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fileds = ('nombre','descripcion')

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fileds = ('nombre')
        
class EntradaDiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntradaDiario
        fileds = ('usuario','categoria','etiquetas','titulo','contenido','fecha','hora','estado_animo','nivel_importancia')
        
class HistorialEntradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistorialEntrada
        fileds = ('entrada','estado_anterior','estado_nuevo','fecha_cambio','comentario')
        # De esta forma nosotros decidimos qué atributos de nuestra clase/modelo se serializarán