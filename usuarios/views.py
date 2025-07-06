from rest_framework import viewsets, filters
from usuarios.models import Usuario, PerfilUsuario
from .serializers import UsuarioSerializer, PerfilUsuarioSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministrador
from auditoria.utils import registrar_log


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
    
    def perform_create(self, serializer):
        instance = serializer.save()
        registrar_log(
            usuario=self.request.user,
            acao='criar',
            entidade='Usuario',
            id_entidade=instance.id,
            descricao=f'Usuario {instance} - {instance.nome_completo} - criado.'
        )

    def perform_update(self, serializer):
        instance = self.get_object()  # Consulta antes da atualização
        dados_antigos = {field: getattr(instance, field) for field in serializer.fields}
        instance = serializer.save()  # Salva e atualiza os dados
        dados_novos = {field: getattr(instance, field) for field in serializer.fields}

        alteracoes = []
        for campo in dados_antigos:
            if dados_antigos[campo] != dados_novos[campo]:
                alteracoes.append(f"{campo}: '{dados_antigos[campo]}' → '{dados_novos[campo]}'")

        descricao = "Atualização do Usuario.\n" + "\n".join(alteracoes) if alteracoes else "Atualização sem mudanças detectadas."

        registrar_log(self.request.user, 'atualizar', 'Usuario', instance.id, descricao)


    def perform_destroy(self, instance):
        registrar_log(self.request.user, 'remover', 'Usuario', instance.id, 'Usuario removido.')
        instance.delete()