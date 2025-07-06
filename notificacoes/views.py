from rest_framework import viewsets
from notificacoes.models import Notificacao
from .serializers import NotificacaoSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministradorOrPaciente

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer
    permission_classes = [IsAuthenticated, IsAdministradorOrPaciente]