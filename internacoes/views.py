from rest_framework import viewsets
from internacoes.models import Internacao, Leito
from .serializers import InternacaoSerializer, LeitoSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministradorOrProfissional
from auditoria.utils import registrar_log

class InternacaoViewSet(viewsets.ModelViewSet):
    queryset = Internacao.objects.all()
    serializer_class = InternacaoSerializer
    permission_classes = [IsAuthenticated, IsAdministradorOrProfissional]

    def get_queryset(self):
        user = self.request.user
        if user.perfil.nome_perfil == 'Paciente':
            return Internacao.objects.filter(paciente__usuario=user)
        elif user.perfil.nome_perfil == 'Profissional de Saúde':
            return Internacao.objects.filter(profissional__usuario=user)
        return Internacao.objects.all()
    
    def perform_create(self, serializer):
        instance = serializer.save()
        registrar_log(
            usuario=self.request.user,
            acao='criar',
            entidade='Internacao',
            id_entidade=instance.id,
            descricao=f'Internação do paciente {instance.paciente} no leito {instance.leito} em {instance.data_entrada}'
        )

    def perform_update(self, serializer):
        instance = self.get_object()  # Dados antes da atualização
        dados_antigos = {field: getattr(instance, field) for field in serializer.fields}
        instance = serializer.save()  # Salva e atualiza os dados
        dados_novos = {field: getattr(instance, field) for field in serializer.fields}

        alteracoes = []
        for campo in dados_antigos:
            if dados_antigos[campo] != dados_novos[campo]:
                alteracoes.append(f"{campo}: '{dados_antigos[campo]}' → '{dados_novos[campo]}'")

        descricao = "Atualização da Internação.\n" + "\n".join(alteracoes) if alteracoes else "Atualização sem mudanças detectadas."

        registrar_log(self.request.user, 'atualizar', 'Internacao', instance.id, descricao)
        if instance.data_saida:
            instance.leito.disponivel = True


    def perform_destroy(self, instance):
        registrar_log(self.request.user, 'remover', 'Internacao', instance.id, 'Internação removida.')
        instance.delete()


class LeitoViewSet(viewsets.ModelViewSet):
    queryset = Leito.objects.all()
    serializer_class = LeitoSerializer
    permission_classes = [IsAuthenticated, IsAdministradorOrProfissional]

    def perform_create(self, serializer):
        instance = serializer.save()
        registrar_log(
            usuario=self.request.user,
            acao='criar',
            entidade='Leito',
            id_entidade=instance.id,
            descricao=f'Leito {instance.leito} criado.'
        )

    def perform_update(self, serializer):
        instance = self.get_object()  # Dados antes da atualização
        dados_antigos = {field: getattr(instance, field) for field in serializer.fields}
        instance = serializer.save()  # Salva e atualiza os dados
        dados_novos = {field: getattr(instance, field) for field in serializer.fields}

        alteracoes = []
        for campo in dados_antigos:
            if dados_antigos[campo] != dados_novos[campo]:
                alteracoes.append(f"{campo}: '{dados_antigos[campo]}' → '{dados_novos[campo]}'")

        descricao = "Atualização do Leito.\n" + "\n".join(alteracoes) if alteracoes else "Atualização sem mudanças detectadas."

        registrar_log(self.request.user, 'atualizar', 'Leito', instance.id, descricao)
      
    def perform_destroy(self, instance):
        registrar_log(self.request.user, 'remover', 'Leito', instance.id, 'Leito removido.')
        instance.delete()
