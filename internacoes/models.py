from django.db import models
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude

class Leito(models.Model):
    numero = models.CharField(max_length=10)
    tipo = models.CharField(max_length=50)
    ala = models.CharField(max_length=100)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"Leito {self.numero} - {self.ala}"

class Internacao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)
    leito = models.ForeignKey(Leito, on_delete=models.PROTECT)
    data_entrada = models.DateTimeField()
    data_saida = models.DateTimeField(null=True, blank=True)
    motivo = models.CharField(max_length=255)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Internação de {self.paciente.usuario.nome_completo} no leito {self.leito.numero}"
