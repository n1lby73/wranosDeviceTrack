from rest_framework.routers import DefaultRouter
from .views import vendorViewSet

router = DefaultRouter()
router.register(r'vendor', vendorViewSet, basename='vendor')

urlpatterns = router.urls
