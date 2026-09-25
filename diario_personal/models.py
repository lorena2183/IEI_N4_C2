
from django.db import models

str_fecha_creacion = "Fecha Creación"
str_fecha_actualizacion = "Fecha Actualización"
str_usuario = "Usuario"
str_entrada ="Entrada"
str_categoria = "Categoria"


class Usuario(models.Model):
    nombre_usuario = models.CharField("Usuario",max_length=25,null=False)
    email = models.EmailField(null=True)
    contrasena = models.CharField(max_length=100,null=False)
    fecha_nacimiento = models.DateField()
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)

    def __str__(self):
        return self.nombre_usuario


class Categoria(models.Model):
    nombre = models.CharField("Categoria",max_length=25,null=False)
    descripcion = models.TextField(max_length=100,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)

    def __str__(self):
        return self.nombre


class Etiqueta(models.Model):
    nombre = models.CharField("Etiqueta",max_length=25,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)

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
    nivel_importancia = models.IntegerField()
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)

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