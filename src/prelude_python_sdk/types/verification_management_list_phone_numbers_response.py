# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel

__all__ = ["VerificationManagementListPhoneNumbersResponse", "PhoneNumber"]


class PhoneNumber(BaseModel):
    created_at: datetime
    """The date and time when the phone number was added to the list."""

    phone_number: str
    """An E.164 formatted phone number."""


class VerificationManagementListPhoneNumbersResponse(BaseModel):
    phone_numbers: List[PhoneNumber]
    """A list of phone numbers in the allow or block list."""
