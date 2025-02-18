from __future__ import annotations

from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Initialize the database with the default data."""

    help = "Initialize the database with the default data"

    def handle(self, *args, **options):
        """Handle the command."""
        User.objects.create_superuser(
            "",
            "jan@zeleny.io",
            password="changeme",  # noqa: S106
        )
