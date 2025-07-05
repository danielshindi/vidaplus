from rest_framework import viewsets
from internacoes.models import Internacao, Leito
from .serializers import InternacaoSerializer, LeitoSerializer

class InternacaoViewSet(viewsets.ModelViewSet):
    queryset = Internacao.objects.all()
    serializer_class = InternacaoSerializer


class LeitoViewSet(viewsets.ModelViewSet):
    queryset = Leito.objects.all()
    serializer_class = LeitoSerializer
