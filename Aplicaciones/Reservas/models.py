from django.db import models
class EspacioEstudio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    capacidad = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    disponible = models.CharField(max_length=100)
class Reserva(models.Model):
    id=models.AutoField(primary_key=True)
    apellido=models.CharField(max_length=100)
    espacio=models.ForeignKey(EspacioEstudio, on_delete=models.CASCADE)
    fecha=models.DateField()
    horainicio=models.TimeField()
    horafin=models.TimeField()
