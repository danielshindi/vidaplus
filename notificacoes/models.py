from django.db import models
from usuarios.models import Usuario

class Notificacao(models.Model):
    TIPO_CHOICES = [
        ('sistema', 'Sistema'),
        ('consulta', 'Consulta'),
        ('receita', 'Receita'),
        ('outro', 'Outro'),
    ]
    CANAL_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('app', 'Aplicativo'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    canal = models.CharField(max_length=50, choices=CANAL_CHOICES)

    def __str__(self):
        return f"{self.titulo} ({self.usuario.matricula})"
