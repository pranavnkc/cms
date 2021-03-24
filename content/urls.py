from rest_framework import routers
from .views import ContentViewSet
router = routers.DefaultRouter()
router.register(r'content', ContentViewSet, basename="content")

urlpatterns = router.urls
