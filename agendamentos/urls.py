from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ConsultaViewSet

router = DefaultRouter()
router.register(r'consultas', ConsultaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
