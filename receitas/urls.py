from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ReceitaViewSet

router = DefaultRouter()
router.register(r'receitas', ReceitaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
