from rest_framework.routers import DefaultRouter
from .views import ProntuarioViewSet

router = DefaultRouter()
router.register(r'', ProntuarioViewSet)

urlpatterns = router.urls