
from django.db import models


class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=25)
    email = models.EmailField()
    contrasena = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    es_publico = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_usuario


class Categoria(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class EntradaDiario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    etiquetas = models.ManyToManyField(Etiqueta, blank=True)
    titulo = models.CharField(max_length=25)
    contenido = models.TextField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    estado_animo = models.CharField(max_length=25)
    es_publica = models.BooleanField(default=False)
    nivel_importancia = models.IntegerField()
    calificacion = models.DecimalField(max_digits=3, decimal_places=1)
    latitud = models.FloatField(null=True, blank=True)
    enlace_referencia = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titulo} ({self.fecha})"


class HistorialEntrada(models.Model):
    entrada = models.ForeignKey(EntradaDiario, on_delete=models.CASCADE)
    estado_anterior = models.CharField(max_length=25)
    estado_nuevo = models.CharField(max_length=25)
    fecha_cambio = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.entrada} : {self.estado_anterior} -> {self.estado_nuevo}"