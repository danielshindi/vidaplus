from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PacienteCompletoViewSet

router = DefaultRouter()
router.register(r'pacientes', PacienteCompletoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
