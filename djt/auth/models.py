from __future__ import annotations

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from djt.auth.managers import CustomUserManager


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_("e-mail"), unique=True)
    photo = models.ImageField(_("photo"), upload_to="users/", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        """Return string representation of object."""
        if full_name := self.get_full_name():
            return full_name
        return self.email
