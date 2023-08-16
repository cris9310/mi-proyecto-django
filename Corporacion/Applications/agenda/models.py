from django.db import models

from Applications.academico.models import User

class Evento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=200, unique=False)
    descripcion = models.TextField()
    start_time = models.DateField(verbose_name='Fecha_inicio')
    end_time = models.DateField(verbose_name='Fecha_final')
    hora_inicio= models.TimeField()
    hora_final= models.TimeField()
    color = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title