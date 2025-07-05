from rest_framework import viewsets
from usuarios.models import Usuario, PerfilUsuario
from .serializers import UsuarioSerializer, PerfilUsuarioSerializer

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer