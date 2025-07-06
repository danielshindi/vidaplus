from rest_framework import viewsets, filters
from usuarios.models import Usuario, PerfilUsuario
from .serializers import UsuarioSerializer, PerfilUsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministrador

class PerfilUsuarioViewSet(viewsets.ModelViewSet):
    queryset = PerfilUsuario.objects.all()
    serializer_class = PerfilUsuarioSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated, IsAdministrador]
    filter_backends = [filters.SearchFilter]
    search_fields = ['matricula', 'nome_completo', 'email', 'cpf']

    def get_queryset(self):
        queryset = super().get_queryset()
        perfil_id = self.request.query_params.get('perfil')
        if perfil_id:
            queryset = queryset.filter(perfil_id=perfil_id)
        return queryset