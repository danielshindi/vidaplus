from django.db import models
from pacientes.models import Paciente

class Prontuario(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='prontuarios')
    descricao = models.TextField()
    data = models.DateField()

    def __str__(self):
        return f"Prontuário de {self.paciente.usuario.nome_completo} em {self.data}"