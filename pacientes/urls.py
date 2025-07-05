from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PacienteViewSet

router = DefaultRouter()
router.register(r'pacientes', PacienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
