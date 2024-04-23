# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationCreateResponse", "Metadata"]


class Metadata(BaseModel):
    correlation_id: Optional[str] = None


class VerificationCreateResponse(BaseModel):
    id: Optional[str] = None
    """The verification identifier."""

    metadata: Optional[Metadata] = None
    """The metadata for this verification."""

    method: Optional[Literal["message"]] = None
    """The method used for verifying this phone number."""

    request_id: Optional[str] = None

    status: Optional[Literal["success", "retry", "blocked"]] = None
    """The status of the verification."""
