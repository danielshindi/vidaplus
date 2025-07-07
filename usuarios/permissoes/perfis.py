from rest_framework.permissions import BasePermission

class IsAdministrador(BasePermission):
    """Permite acesso apenas a usuários com perfil Administrador."""
    def has_permission(self, request, view):
        return hasattr(request.user, 'perfil') and request.user.perfil.nome_perfil == 'Administrador'


class IsProfissionalSaude(BasePermission):
    """Permite acesso apenas a profissionais de saúde."""
    def has_permission(self, request, view):
        return hasattr(request.user, 'perfil') and request.user.perfil.nome_perfil == 'Profissional'


class IsPaciente(BasePermission):
    """Permite acesso apenas a pacientes."""
    def has_permission(self, request, view):
        return hasattr(request.user, 'perfil') and request.user.perfil.nome_perfil == 'Paciente'


class IsAdministradorOrProfissional(BasePermission):
    """Permite acesso a administradores ou profissionais de saúde."""
    def has_permission(self, request, view):
        return (
            hasattr(request.user, 'perfil') and
            request.user.perfil.nome_perfil in ['Administrador', 'Profissional']
        )


class IsAdministradorOrPaciente(BasePermission):
    """Permite acesso a administradores ou pacientes."""
    def has_permission(self, request, view):
        return (
            hasattr(request.user, 'perfil') and
            request.user.perfil.nome_perfil in ['Administrador', 'Paciente']
        )


class IsPacienteOrProfissional(BasePermission):
    """Permite acesso a pacientes ou profissionais."""
    def has_permission(self, request, view):
        return (
            hasattr(request.user, 'perfil') and
            request.user.perfil.nome_perfil in ['Paciente', 'Profissional']
        )

class IsSelfOrAdmin(BasePermission):
    """
    Permite acesso se for o próprio usuário ou administrador.
    """
    def has_object_permission(self, request, view, obj):
        if hasattr(request.user, 'perfil') and request.user.perfil.nome_perfil == 'Administrador':
            return True
        return obj.usuario == request.user