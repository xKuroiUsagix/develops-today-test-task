from rest_framework.routers import DefaultRouter

from .views import SpyCatViewSet


router = DefaultRouter()
router.register('spy_cats', SpyCatViewSet, basename='spy_cats')

urlpatterns = router.urls
