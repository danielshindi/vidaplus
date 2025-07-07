from rest_framework import viewsets
from pacientes.models import Paciente
from .serializers import PacienteSerializer, PacienteCompletoSerializer
from rest_framework.permissions import IsAuthenticated
from usuarios.permissoes.perfis import IsAdministrador
from auditoria.utils import registrar_log

class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    permission_classes = [IsAuthenticated, IsAdministrador]

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return PacienteCompletoSerializer
        return PacienteSerializer


    def perform_create(self, serializer):
        instance = serializer.save()
        registrar_log(
            usuario=self.request.user,
            acao='criar',
            entidade='Paciente',
            id_entidade=instance.id,
            descricao=f'Paciente {instance} registrado.'
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

        descricao = "Atualização do Paciente.\n" + "\n".join(alteracoes) if alteracoes else "Atualização sem mudanças detectadas."

        registrar_log(self.request.user, 'atualizar', 'Paciente', instance.id, descricao)


    def perform_destroy(self, instance):
        registrar_log(self.request.user, 'remover', 'Paciente', instance.id, 'Paciente removido.')
        instance.delete()


class PacienteCompletoViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all().select_related('usuario')
    serializer_class = PacienteCompletoSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save()
        registrar_log(
            usuario=self.request.user,
            acao='criar',
            entidade='Paciente',
            id_entidade=instance.id,
            descricao=f'Paciente {instance} registrado.'
        )

    def perform_update(self, serializer):
        instance = self.get_object()  # Consulta antes da atualização

        # Captura os dados antigos do paciente
        dados_antigos = {field: getattr(instance, field) for field in serializer.fields}

        # Captura os dados antigos do usuário
        usuario_antigo = instance.usuario
        usuario_antigo_dados = {
            'matricula': usuario_antigo.matricula,
            'nome_completo': usuario_antigo.nome_completo,
            'email': usuario_antigo.email,
            'cpf': usuario_antigo.cpf,
            'telefone': usuario_antigo.telefone,
            'nascimento': usuario_antigo.nascimento,
            'endereco': usuario_antigo.endereco,
            'perfil': usuario_antigo.perfil_id,
        }

        # Salva as alterações
        instance = serializer.save()

        # Captura os dados novos do paciente
        dados_novos = {field: getattr(instance, field) for field in serializer.fields}

        # Captura os dados novos do usuário
        usuario_novo = instance.usuario
        usuario_novo_dados = {
            'matricula': usuario_novo.matricula,
            'nome_completo': usuario_novo.nome_completo,
            'email': usuario_novo.email,
            'cpf': usuario_novo.cpf,
            'telefone': usuario_novo.telefone,
            'nascimento': usuario_novo.nascimento,
            'endereco': usuario_novo.endereco,
            'perfil': usuario_novo.perfil_id,
        }

        # Compara alterações no paciente
        alteracoes = []
        for campo in dados_antigos:
            if campo == 'usuario':
                continue  # já vamos tratar separadamente
            if dados_antigos[campo] != dados_novos[campo]:
                alteracoes.append(f"{campo}: '{dados_antigos[campo]}' → '{dados_novos[campo]}'")

        # Compara alterações no usuário
        for campo in usuario_antigo_dados:
            if usuario_antigo_dados[campo] != usuario_novo_dados[campo]:
                alteracoes.append(f"usuario.{campo}: '{usuario_antigo_dados[campo]}' → '{usuario_novo_dados[campo]}'")

        # Monta a descrição do log
        descricao = "Atualização do Paciente.\n" + "\n".join(alteracoes) if alteracoes else "Atualização sem mudanças detectadas."

        # Registra o log
        registrar_log(self.request.user, 'atualizar', 'Paciente', instance.id, descricao)



    def perform_destroy(self, instance):
        registrar_log(self.request.user, 'remover', 'Paciente', instance.id, 'Paciente removido.')
        instance.delete()

