from rest_framework.routers import DefaultRouter
from .views import customerViewSet

router = DefaultRouter()
router.register(r'customer', customerViewSet, basename='customer')

urlpatterns = router.urls
