from django.db import models
from usuarios.models import Usuario

class LogEntry(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='logentries_auditoria')
    timestamp = models.DateTimeField(auto_now_add=True)
    acao = models.CharField(max_length=100)
    entidade = models.CharField(max_length=100)
    id_entidade = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return f"[{self.timestamp}] {self.usuario.matricula} - {self.acao} em {self.entidade}#{self.id_entidade}"
