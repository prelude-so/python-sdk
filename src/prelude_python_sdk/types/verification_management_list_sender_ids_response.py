# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["VerificationManagementListSenderIDsResponse", "VerificationManagementListSenderIDsResponseItem"]


class VerificationManagementListSenderIDsResponseItem(BaseModel):
    status: Optional[Literal["approved", "pending", "rejected"]] = None
    """It indicates the status of the sender ID. Possible values are:

    - `approved` - The sender ID is approved.
    - `pending` - The sender ID is pending.
    - `rejected` - The sender ID is rejected.
    """

    value: Optional[str] = None
    """Value that will be presented as Sender ID"""


VerificationManagementListSenderIDsResponse: TypeAlias = List[VerificationManagementListSenderIDsResponseItem]
