
from django.db import models

class Inscrito(models.Model):
    ESTADOS = (
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No Asisten'),
    )

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha_inscripcion = models.DateField()
    institucion = models.CharField(max_length=100)
    hora_inscripcion = models.TimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS)
    observacion = models.TextField(blank=True)
