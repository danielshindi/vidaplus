from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import LogEntryViewSet

router = DefaultRouter()
router.register(r'logs', LogEntryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]