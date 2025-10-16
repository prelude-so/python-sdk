# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationManagementListSenderIDsResponse", "SenderID"]


class SenderID(BaseModel):
    sender_id: Optional[str] = None
    """Value that will be presented as Sender ID"""

    status: Optional[Literal["approved", "pending", "rejected"]] = None
    """It indicates the status of the Sender ID. Possible values are:

    - `approved` - The Sender ID is approved.
    - `pending` - The Sender ID is pending.
    - `rejected` - The Sender ID is rejected.
    """


class VerificationManagementListSenderIDsResponse(BaseModel):
    sender_ids: Optional[List[SenderID]] = None
