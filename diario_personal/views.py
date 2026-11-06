from functools import wraps

from django.shortcuts import render, redirect
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

from .forms import EntradaDiarioForm


# ======================================================
def login_requerido(vista):
    @wraps(vista)
    def envoltura(request, *args, **kwargs):
        if not request.session.get('usuario_id'):
            return redirect('inicio')
        return vista(request, *args, **kwargs)
    return envoltura


# ======================================================
#  PÁGINAS WEB
# ======================================================
def inicio(request):
    """Pantalla de bienvenida = login contra la tabla Usuario."""
    if request.session.get('usuario_id'):
        return redirect('entradas')

    error = None
    if request.method == 'POST':
        nombre = request.POST.get('nombre_usuario', '').strip()
        clave = request.POST.get('contrasena', '')
        usuario = Usuario.objects.filter(nombre_usuario=nombre, contrasena=clave).first()
        if usuario:
            request.session['usuario_id'] = usuario.id
            return redirect('entradas')
        error = 'Usuario o contraseña incorrectos. Intenta de nuevo 🌷'

    return render(request, 'diario_personal/inicio.html', {'error': error})


def salir(request):
    request.session.flush()
    return redirect('inicio')


# ---------- Listas ----------
@login_requerido
def lista_usuarios(request):
    usuarios = Usuario.objects.all().order_by('nombre_usuario')
    return render(request, 'diario_personal/usuarios/usuario_lista.html', {'usuarios': usuarios})


@login_requerido
def lista_categorias(request):
    categorias = Categoria.objects.all().order_by('nombre')
    return render(request, 'diario_personal/categorias/categoria_lista.html', {'categorias': categorias})


@login_requerido
def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all().order_by('nombre')
    return render(request, 'diario_personal/etiquetas/etiqueta_lista.html', {'etiquetas': etiquetas})


@login_requerido
def lista_entradas(request):
    """Lista de entradas del usuario que inició sesión (es su diario)."""
    usuario = Usuario.objects.filter(id=request.session['usuario_id']).first()
    if usuario is None:               # el usuario fue borrado: se cierra la sesión
        request.session.flush()
        return redirect('inicio')
    entradas = (EntradaDiario.objects
                .filter(usuario=usuario)
                .select_related('categoria')
                .prefetch_related('etiquetas')
                .order_by('-fecha', '-hora'))
    return render(request, 'diario_personal/entradas/entrada_lista.html',
                  {'entradas': entradas, 'usuario': usuario})


@login_requerido
def lista_historial(request):
    historial = (HistorialEntrada.objects
                 .select_related('entrada')
                 .order_by('-fecha_cambio'))
    return render(request, 'diario_personal/historial/historial_lista.html', {'historial': historial})


# ---------- Formulario ----------
@login_requerido
def crear_entrada(request):
    if request.method == 'POST':
        form = EntradaDiarioForm(request.POST)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.usuario_id = request.session['usuario_id']
            entrada.save()
            form.save_m2m()           # guarda las etiquetas
            return redirect('entradas')
    else:
        form = EntradaDiarioForm()
    return render(request, 'diario_personal/entrada_form.html', {'form': form})


# ======================================================
#  API (lo que ya tenías, sin cambios)
# ======================================================
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
