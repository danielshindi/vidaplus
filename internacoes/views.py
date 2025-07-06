from rest_framework import viewsets
from internacoes.models import Internacao, Leito
from .serializers import InternacaoSerializer, LeitoSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministradorOrProfissional

class InternacaoViewSet(viewsets.ModelViewSet):
    queryset = Internacao.objects.all()
    serializer_class = InternacaoSerializer
    permission_classes = [IsAuthenticated, IsAdministradorOrProfissional]


class LeitoViewSet(viewsets.ModelViewSet):
    queryset = Leito.objects.all()
    serializer_class = LeitoSerializer
    permission_classes = [IsAuthenticated, IsAdministradorOrProfissional]
