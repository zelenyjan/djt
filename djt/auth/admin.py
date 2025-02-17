from __future__ import annotations

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import gettext_lazy as _

from djt.auth.models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    """User admin."""

    list_display = [
        "email",
        "__str__",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]
    ordering = ["email"]
    search_fields = ["email", "first_name", "last_name"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        (_("Personal info"), {"fields": ["first_name", "last_name", "photo"]}),
        (
            _("Permissions"),
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ],
            },
        ),
        (_("Important dates"), {"fields": ["last_login", "date_joined"]}),
    ]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "usable_password", "password1", "password2"),
            },
        ),
    )
