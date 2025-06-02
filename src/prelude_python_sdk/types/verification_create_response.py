# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationCreateResponse", "Metadata", "Silent"]


class Metadata(BaseModel):
    correlation_id: Optional[str] = None


class Silent(BaseModel):
    request_url: str
    """The URL to start the silent verification towards."""


class VerificationCreateResponse(BaseModel):
    id: str
    """The verification identifier."""

    method: Literal["message", "silent", "voice"]
    """The method used for verifying this phone number."""

    status: Literal["success", "retry", "blocked"]
    """The status of the verification."""

    channels: Optional[List[str]] = None
    """The ordered sequence of channels to be used for verification"""

    metadata: Optional[Metadata] = None
    """The metadata for this verification."""

    reason: Optional[
        Literal["suspicious", "repeated_attempts", "invalid_phone_line", "invalid_phone_number", "in_block_list"]
    ] = None
    """The reason why the verification was blocked.

    Only present when status is "blocked".
    """

    request_id: Optional[str] = None

    silent: Optional[Silent] = None
    """The silent verification specific properties."""
