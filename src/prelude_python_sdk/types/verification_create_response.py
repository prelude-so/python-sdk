# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationCreateResponse", "Metadata"]


class Metadata(BaseModel):
    correlation_id: Optional[str] = None


class VerificationCreateResponse(BaseModel):
    id: str
    """The verification identifier."""

    method: Literal["message"]
    """The method used for verifying this phone number."""

    status: Literal["success", "retry", "blocked"]
    """The status of the verification."""

    metadata: Optional[Metadata] = None
    """The metadata for this verification."""

    request_id: Optional[str] = None
