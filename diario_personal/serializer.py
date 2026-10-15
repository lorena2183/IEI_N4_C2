from rest_framework import serializers

from .models import Usuario
from .models import Categoria
from .models import Etiqueta
from .models import EntradaDiario
from .models import HistorialEntrada

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        # __all__ serializa todas los atributos de la clase/modelo

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'

class EntradaDiarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntradaDiario
        fields = '__all__'

class HistorialEntradaSerializer(serializers.ModelSerializer):