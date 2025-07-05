from rest_framework import viewsets
from relatorios.models import Relatorio
from .serializers import RelatorioSerializer

class RelatorioViewSet(viewsets.ModelViewSet):
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer