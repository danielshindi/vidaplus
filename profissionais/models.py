from django.db import models
from usuarios.models import Usuario

class ProfissionalSaude(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    especialidade = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.usuario.nome_completo} - {self.especialidade}"
