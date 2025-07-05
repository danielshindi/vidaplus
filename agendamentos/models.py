from django.db import models
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude

class Consulta(models.Model):
    STATUS_CHOICES = [
        ('agendada', 'Agendada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE, related_name='consultas')
    data_hora = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='agendada')

    def __str__(self):
        return f"Consulta de {self.paciente.usuario.nome_completo} com {self.profissional.usuario.nome_completo} em {self.data_hora.strftime('%d/%m/%Y %H:%M')}"
