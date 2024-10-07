from django.db import models
from estilos.models import Estilos

class Cantores(models.Model):
    cantor = models.CharField (max_length=100, null=False,blank=False)
    tipo = models.ForeignKey(Estilos, on_delete=models.CASCADE, default='SP')

    def __str__(self) -> str:
        return self.cantor