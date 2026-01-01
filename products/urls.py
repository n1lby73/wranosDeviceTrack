from rest_framework.routers import DefaultRouter
from .views import productViewSet

router = DefaultRouter()
router.register(r'product', productViewSet, basename='product')

urlpatterns = router.urls
