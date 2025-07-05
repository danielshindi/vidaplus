from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UsuarioViewSet, PerfilUsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'perfis', PerfilUsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
