from __future__ import annotations

from io import BytesIO

from django.core.files.images import ImageFile
from django.db import models
from django.utils.text import slugify

import httpx

from djt.ai_samples.client import openai_client


class Image(models.Model):
    """Image model."""

    prompt = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/", null=True, editable=False)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self) -> str:
        """Return the prompt."""
        return self.prompt

    def save(self, *args, **kwargs):
        """Save the image."""
        image_url = openai_client.generate_image(self.prompt)
        image_data = httpx.get(image_url).content
        content = BytesIO(image_data)
        content.seek(0)
        image = ImageFile(content, name=f"{slugify(self.prompt)}.png")
        self.image = image
        super().save(*args, **kwargs)


class Text(models.Model):
    """Text model."""

    class ModelChoices(models.TextChoices):
        """Model choices."""

        GPT_4O_MINI = "gpt-4o-mini", "gpt-4o-mini"
        GPT_4O = "gpt-4o", "gpt-4o"

    prompt = models.CharField(max_length=255)
    model = models.CharField(max_length=255, choices=ModelChoices.choices, default=ModelChoices.GPT_4O_MINI)
    response = models.TextField(default="", editable=False)

    def __str__(self) -> str:
        """Return the prompt."""
        return self.prompt

    def save(self, *args, **kwargs):
        """Save the response."""
        self.response = openai_client.generate_message(self.model, self.prompt)
        super().save(*args, **kwargs)
