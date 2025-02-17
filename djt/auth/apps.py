from __future__ import annotations

from django.apps import AppConfig


class AuthConfig(AppConfig):
    """Auth app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "djt.auth"
    label = "djt_auth"
