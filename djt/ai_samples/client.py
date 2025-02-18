from __future__ import annotations

from django.conf import settings

from openai import OpenAI


class Client:
    """OpenAI client."""

    def __init__(self):
        """Initialize the client."""
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def generate_image(self, prompt: str) -> str:
        """Generate an image."""
        response = self.client.images.generate(
            prompt=prompt,
            model="dall-e-3",
            quality="standard",
            n=1,
            size="1024x1024",
        )
        return response.data[0].url

    def generate_message(self, model: str, prompt: str) -> str:
        """Generate a message."""
        completion = self.client.chat.completions.create(model=model, messages=[{"role": "user", "content": prompt}])
        return completion.choices[0].message.content


openai_client = Client()
