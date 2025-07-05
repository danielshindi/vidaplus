# App: usuarios.management.commands.popular_dados
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
import random

from usuarios.models import Usuario, PerfilUsuario
from pacientes.models import Paciente
from profissionais.models import ProfissionalSaude
from agendamentos.models import Consulta
from telemedicina.models import Teleconsulta
from internacoes.models import Internacao, Leito
from relatorios.models import Relatorio
from notificacoes.models import Notificacao
from auditoria.models import LogEntry
from django.db import transaction

# novos imports
from relatorios.models import Relatorio
from notificacoes.models import Notificacao
from auditoria.models import LogEntry
from agendamentos.models import Consulta
from telemedicina.models import Teleconsulta
from internacoes.models import Internacao, Leito
from profissionais.models import ProfissionalSaude
from pacientes.models import Paciente
from receitas.models import Receita
from prontuarios.models import Prontuario

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados fictícios para testes.'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        # Limpar dados antigos
        LogEntry.objects.all().delete()
        Notificacao.objects.all().delete()
        Internacao.objects.all().delete()
        Teleconsulta.objects.all().delete()
        Consulta.objects.all().delete()
        Receita.objects.all().delete()
        Prontuario.objects.all().delete()
        Leito.objects.all().delete()
        ProfissionalSaude.objects.all().delete()
        Paciente.objects.all().delete()
        Usuario.objects.exclude(is_superuser=True).delete()
        PerfilUsuario.objects.all().delete()

        # Criar perfis
        perfil_paciente, _ = PerfilUsuario.objects.get_or_create(nome_perfil='Paciente')
        perfil_profissional, _ = PerfilUsuario.objects.get_or_create(nome_perfil='Profissional')
        perfil_admin, _ = PerfilUsuario.objects.get_or_create(nome_perfil='Administrador')

        # Criar pacientes
        pacientes = []
        for i in range(5):
            usuario = Usuario.objects.create_user(
                matricula=f'PAC00{i}',
                password='senha123',
                nome_completo=f'Paciente {i}',
                email=f'paciente{i}@mail.com',
                cpf=f'0000000000{i}',
                telefone='(11) 90000-0000',
                nascimento='1990-01-01',
                endereco='Rua dos Testes, 100',
                perfil=perfil_paciente,
            )
            paciente = Paciente.objects.create(usuario=usuario, genero='Outro', convenio='Plano Saúde')
            pacientes.append(paciente)

        # Criar profissionais
        profissionais = []
        for i in range(3):
            usuario = Usuario.objects.create_user(
                matricula=f'PROF00{i}',
                password='senha123',
                nome_completo=f'Dr. Profissional {i}',
                email=f'prof{i}@mail.com',
                cpf=f'1111111111{i}',
                telefone='(11) 98888-0000',
                nascimento='1985-01-01',
                endereco='Av. Clínica, 456',
                perfil=perfil_profissional,
            )
            profissional = ProfissionalSaude.objects.create(usuario=usuario, especialidade='Clínico Geral', departamento='Clínica Médica')
            profissionais.append(profissional)

        # Criar leitos
        leitos = []
        for i in range(3):
            leito = Leito.objects.create(numero=f'{100+i}', tipo='Enfermaria', ala='Ala A', disponivel=True)
            leitos.append(leito)

        # Criar consultas, receitas, prontuários, teleconsultas, internações, notificações e logs
        for i in range(5):
            paciente = random.choice(pacientes)
            profissional = random.choice(profissionais)

            data_consulta = timezone.now() + timedelta(days=i)
            consulta = Consulta.objects.create(
                paciente=paciente,
                profissional=profissional,
                data_hora=data_consulta,
                status='agendada'
            )

            # Criar receita
            Receita.objects.create(
                paciente=paciente,
                profissional=profissional,
                data_emissao=data_consulta,
                prescricao='Paracetamol 500mg de 8 em 8h por 5 dias.'
            )

            # Criar prontuário
            Prontuario.objects.create(
                paciente=paciente,
                descricao='Paciente relatou dor de cabeça. Exame físico sem alterações.',
                data=data_consulta.date()
            )

            # Criar teleconsulta associada a algumas consultas
            if i % 2 == 0:
                Teleconsulta.objects.create(
                    consulta=consulta,
                    paciente=paciente,
                    profissional=profissional,
                    inicio=data_consulta,
                    fim=data_consulta + timedelta(minutes=30),
                    url_video='https://teleconsulta.exemplo.com/sala1',
                    status='agendada',
                    token_acesso='token123'
                )

            # Criar internação
            if i % 3 == 0:
                Internacao.objects.create(
                    paciente=paciente,
                    profissional=profissional,
                    leito=random.choice(leitos),
                    data_entrada=timezone.now() - timedelta(days=1),
                    data_saida=None,
                    motivo='Observação',
                    observacoes='Paciente em observação clínica.'
                )

            # Criar notificação
            Notificacao.objects.create(
                usuario=paciente.usuario,
                titulo='Lembrete de Consulta',
                mensagem='Você tem uma consulta agendada.',
                tipo='consulta',
                canal='email'
            )

            # Criar relatório fictício
            Relatorio.objects.create(
                administrador=profissional.usuario,
                titulo='Atendimentos Semanais',
                tipo='Consulta',
                conteudo='Relatório com número de atendimentos realizados na semana.'
            )

            # Criar log
            LogEntry.objects.create(
                usuario=profissional.usuario,
                acao='Criar Consulta',
                entidade='Consulta',
                id_entidade=str(consulta.id),
                descricao='Consulta agendada pelo profissional.'
            )

        self.stdout.write(self.style.SUCCESS('Base de testes populada com sucesso.'))
