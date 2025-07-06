from auditoria.models import LogEntry

def registrar_log(usuario, acao, entidade, id_entidade, descricao=''):
    LogEntry.objects.create(
        usuario=usuario,
        acao=acao,
        entidade=entidade,
        id_entidade=str(id_entidade),
        descricao=descricao
    )