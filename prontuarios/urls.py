from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProntuarioViewSet, HistoricoMedicoView

router = DefaultRouter()
router.register(r'', ProntuarioViewSet)

urlpatterns = [
    path('historico/', HistoricoMedicoView.as_view(), name='historico-medico'),
    path('', include(router.urls)),
]