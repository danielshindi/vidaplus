from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ProntuarioViewSet

router = DefaultRouter()
router.register(r'prontuarios', ProntuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
