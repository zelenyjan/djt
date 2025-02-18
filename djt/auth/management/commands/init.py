from __future__ import annotations

from django.core.management import BaseCommand

from djt.auth.models import User


class Command(BaseCommand):
    """Initialize the database with the default data."""

    help = "Initialize the database with the default data"

    def handle(self, *args, **options):
        """Handle the command."""
        try:
            User.objects.get(email="jan@zeleny.io")
        except User.DoesNotExist:
            User.objects.create_superuser(
                "jan@zeleny.io",
                password="changeme",  # noqa: S106
            )
