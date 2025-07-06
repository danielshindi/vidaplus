from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TeleconsultaViewSet

router = DefaultRouter()
router.register(r'teleconsultas', TeleconsultaViewSet)

urlpatterns = router.urls