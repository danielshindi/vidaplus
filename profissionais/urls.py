from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProfissionalSaudeViewSet

router = DefaultRouter()
router.register(r'', ProfissionalSaudeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
