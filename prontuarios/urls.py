from rest_framework.routers import DefaultRouter
from .views import ProntuarioViewSet

router = DefaultRouter()
router.register(r'prontuarios', ProntuarioViewSet)

urlpatterns = router.urls