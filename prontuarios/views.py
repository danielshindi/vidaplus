from rest_framework import viewsets
from prontuarios.models import Prontuario
from .serializers import ProntuarioSerializer

class ProntuarioViewSet(viewsets.ModelViewSet):
    queryset = Prontuario.objects.all()
    serializer_class = ProntuarioSerializer
