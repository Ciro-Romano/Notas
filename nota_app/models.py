from django.db import models

class Nota(models.Model):

    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo