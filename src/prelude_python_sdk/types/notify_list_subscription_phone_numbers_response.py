# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NotifyListSubscriptionPhoneNumbersResponse", "PhoneNumber"]


class PhoneNumber(BaseModel):
    config_id: str
    """The subscription configuration ID."""

    phone_number: str
    """The phone number in E.164 format."""

    source: Literal["MO_KEYWORD", "API", "CSV_IMPORT", "CARRIER_DISCONNECT"]
    """How the subscription state was changed:

    - `MO_KEYWORD` - User sent a keyword (STOP/START)
    - `API` - Changed via API
    - `CSV_IMPORT` - Imported from CSV
    - `CARRIER_DISCONNECT` - Automatically unsubscribed due to carrier disconnect
    """

    state: Literal["SUB", "UNSUB"]
    """The subscription state:

    - `SUB` - Subscribed (user can receive marketing messages)
    - `UNSUB` - Unsubscribed (user has opted out)
    """

    updated_at: datetime
    """The date and time when the subscription status was last updated."""

    reason: Optional[str] = None
    """Additional context about the state change (e.g., the keyword that was sent)."""


class NotifyListSubscriptionPhoneNumbersResponse(BaseModel):
    phone_numbers: List[PhoneNumber]
    """A list of phone numbers and their subscription statuses."""

    next_cursor: Optional[str] = None
    """Pagination cursor for the next page of results.

    Omitted if there are no more pages.
    """
