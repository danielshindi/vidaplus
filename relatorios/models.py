from django.db import models
from usuarios.models import Usuario

class Relatorio(models.Model):
    administrador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=100)
    gerado_em = models.DateTimeField(auto_now_add=True)
    conteudo = models.TextField()

    def __str__(self):
        return f"{self.titulo} ({self.tipo}) - {self.gerado_em.strftime('%d/%m/%Y %H:%M')}"