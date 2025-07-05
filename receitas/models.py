from django.db import models
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude

class Receita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='receitas')
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE, related_name='receitas_emitidas')
    data_emissao = models.DateTimeField()
    prescricao = models.TextField()

    def __str__(self):
        return f"Receita para {self.paciente.usuario.nome_completo} - {self.data_emissao.strftime('%d/%m/%Y')}"
