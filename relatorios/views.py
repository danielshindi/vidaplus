from rest_framework import viewsets
from relatorios.models import Relatorio
from .serializers import RelatorioSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministrador

class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]

    def perform_create(self, serializer):
        serializer.save(administrador=self.request.user.administrador)