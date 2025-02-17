from __future__ import annotations

from django.contrib.auth.models import Group

from rest_framework import serializers

from djt.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """User serializer."""

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "date_joined",
            "photo",
        ]


class GroupSerializer(serializers.ModelSerializer):
    """Group serializer."""

    class Meta:
        model = Group
        fields = [
            "id",
            "name",
        ]
