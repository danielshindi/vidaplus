from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RelatorioViewSet

router = DefaultRouter()
router.register(r'relatorios', RelatorioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]