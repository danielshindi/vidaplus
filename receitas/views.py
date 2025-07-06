from rest_framework import viewsets

from receitas.models import Receita
from .serializers import ReceitaSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsProfissionalSaude

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer
    permission_classes = [IsAuthenticated, IsProfissionalSaude]
