from __future__ import annotations

from azure.identity import DefaultAzureCredential
from storages.backends.azure_storage import AzureStorage


class MediaStorage(AzureStorage):
    """Azure media storage."""

    token_credential = DefaultAzureCredential()
    account_name = "djt"
    azure_container = "media"
