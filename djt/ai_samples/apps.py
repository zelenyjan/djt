from __future__ import annotations

from django.apps import AppConfig


class AiSamplesConfig(AppConfig):
    """AI samples app config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "djt.ai_samples"
    verbose_name = "AI Samples"
