# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationManagementSubmitSenderIDResponse"]


class VerificationManagementSubmitSenderIDResponse(BaseModel):
    sender_id: str
    """The sender ID that was added."""

    status: Literal["approved", "pending", "rejected"]
    """It indicates the status of the sender ID. Possible values are:

    - `approved` - The sender ID is approved.
    - `pending` - The sender ID is pending.
    - `rejected` - The sender ID is rejected.
    """

    reason: Optional[str] = None
    """The reason why the sender ID was rejected."""
