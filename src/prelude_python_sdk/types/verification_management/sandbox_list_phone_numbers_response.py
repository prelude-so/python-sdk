# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SandboxListPhoneNumbersResponse", "PhoneNumber"]


class PhoneNumber(BaseModel):
    attempt_code: str
    """The fixed attempt code associated with the sandbox phone number."""

    created_at: datetime
    """The date and time when the phone number was added to the sandbox list."""

    phone_number: str
    """An E.164 formatted phone number."""


class SandboxListPhoneNumbersResponse(BaseModel):
    phone_numbers: List[PhoneNumber]
    """A list of sandbox phone numbers."""
