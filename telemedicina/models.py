from django.db import models
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude
from agendamentos.models import Consulta

class Teleconsulta(models.Model):
    STATUS_CHOICES = [
        ('agendada', 'Agendada'),
        ('em_andamento', 'Em andamento'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada'),
    ]

    consulta = models.OneToOneField(Consulta, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)
    inicio = models.DateTimeField()
    fim = models.DateTimeField(null=True, blank=True)
    url_video = models.URLField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='agendada')
    token_acesso = models.CharField(max_length=255)

    def __str__(self):
        return f"Teleconsulta {self.consulta.id} - {self.status}"
