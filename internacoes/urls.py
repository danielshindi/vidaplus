from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import InternacaoViewSet, LeitoViewSet

router = DefaultRouter()
router.register(r'internacoes', InternacaoViewSet)
router.register(r'leitos', LeitoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
