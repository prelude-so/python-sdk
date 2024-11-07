# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationCheckResponse", "Metadata"]


class Metadata(BaseModel):
    correlation_id: Optional[str] = None


class VerificationCheckResponse(BaseModel):
    id: Optional[str] = None
    """The verification identifier."""

    metadata: Optional[Metadata] = None
    """The metadata for this verification."""

    status: Optional[Literal["success", "failure", "expired"]] = None
    """The status of the check."""
