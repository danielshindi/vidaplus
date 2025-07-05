# App: pacientes
from django.db import models
from usuarios.models import Usuario

class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    genero = models.CharField(max_length=20)
    convenio = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.usuario.nome_completo} ({self.usuario.matricula})"