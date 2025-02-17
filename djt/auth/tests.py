from __future__ import annotations

import pytest

from djt.auth.models import User


@pytest.mark.django_db
class TestUserModel:
    """Test user model."""

    @pytest.fixture
    def user_without_name(self):
        """User without first and last name."""
        return User.objects.create_user(email="user@test.com", password="password")  # noqa: S106

    @pytest.fixture
    def user_with_name(self):
        """User with first and last name."""
        return User.objects.create_user(
            email="user@test.com",
            first_name="John",
            last_name="Doe",
            password="password",  # noqa: S106
        )

    def test_user_without_name(self, user_without_name):
        """Test user without first and last name."""
        assert str(user_without_name) == "user@test.com"

    def test_user_with_name(self, user_with_name):
        """Test user with first and last name."""
        assert str(user_with_name) == "John Doe"
