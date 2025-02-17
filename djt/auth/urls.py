from __future__ import annotations

from rest_framework import routers

from djt.auth.views import GroupViewSet, UserViewSet

app_name = "djt_auth"

router = routers.SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("groups", GroupViewSet, basename="groups")
urlpatterns = router.urls
