from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from notificacoes.models import Notificacao
from .serializers import NotificacaoSerializer
from rest_framework.permissions import IsAuthenticated

class NotificacaoViewSet(viewsets.ModelViewSet):
    queryset = Notificacao.objects.all()
    serializer_class = NotificacaoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.perfil.nome_perfil == 'Administrador':
            return Notificacao.objects.all()
        return Notificacao.objects.filter(usuario=user)
    
    @action(detail=True, methods=['patch'])
    def marcar_como_lida(self, request, pk=None):
        notificacao = self.get_object()
        notificacao.lida = True
        notificacao.save()
        return Response({'status': 'notificação marcada como lida'})
    
    def perform_create(self, serializer):
        instance = serializer.save()
        Notificacao.objects.create(
            usuario=instance.paciente.usuario,
            titulo="Consulta agendada",
            mensagem=f"Sua consulta com {instance.profissional.usuario.nome_completo} está marcada para {instance.data_hora}.",
            tipo="consulta",
            canal="sistema"
        )