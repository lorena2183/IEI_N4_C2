from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Usuario
from .models import Categoria
from .models import Etiqueta
from .models import EntradaDiario
from .models import HistorialEntrada

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Categoria)
admin.site.register(Etiqueta)
admin.site.register(EntradaDiario)
admin.site.register(HistorialEntrada) 
