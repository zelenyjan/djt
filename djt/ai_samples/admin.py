from __future__ import annotations

from django.contrib import admin
from django.utils.safestring import mark_safe

from djt.ai_samples.models import Image, Text


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """Image admin."""

    list_display = ["prompt"]

    def get_readonly_fields(self, request, obj=None):
        """Get readonly fields."""
        if obj and obj.pk:
            return ["prompt", "image", "display_image"]
        return ["image"]

    @admin.display(description="Image")
    def display_image(self, obj: Image | None) -> str:
        """Display image."""
        if not obj.image:
            return "---"
        return mark_safe(f'<img src="{obj.image.url}" width="300" height="300" />')  # noqa: S308


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    """Text admin."""

    list_display = ["prompt", "model"]

    def get_readonly_fields(self, request, obj=None):
        """Get readonly fields."""
        if obj and obj.pk:
            return ["prompt", "model", "response"]
        return ["response"]
