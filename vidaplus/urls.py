"""
URL configuration for vidaplus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios.views import UsuarioViewSet, PerfilUsuarioViewSet
from pacientes.views import PacienteViewSet
from profissionais.views import ProfissionalSaudeViewSet
from agendamentos.views import ConsultaViewSet
from telemedicina.views import TeleconsultaViewSet
from internacoes.views import InternacaoViewSet, LeitoViewSet
from receitas.views import ReceitaViewSet
from prontuarios.views import ProntuarioViewSet
from notificacoes.views import NotificacaoViewSet
from relatorios.views import RelatorioViewSet
from auditoria.views import LogEntryViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'perfis', PerfilUsuarioViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'profissionais', ProfissionalSaudeViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'teleconsultas', TeleconsultaViewSet)
router.register(r'internacoes', InternacaoViewSet)
router.register(r'leitos', LeitoViewSet)
router.register(r'receitas', ReceitaViewSet)
router.register(r'prontuarios', ProntuarioViewSet)
router.register(r'notificacoes', NotificacaoViewSet)
router.register(r'relatorios', RelatorioViewSet)
router.register(r'logs', LogEntryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
