from rest_framework import routers

from api.views import UserViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'users', UserViewSet, base_name='users')

urlpatterns = router.urls
