from __future__ import annotations

from django.contrib.auth.models import Group

from rest_framework import mixins, viewsets

from djt.auth.models import User
from djt.auth.serializers import GroupSerializer, UserSerializer


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """User view set."""

    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """Group view set."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
