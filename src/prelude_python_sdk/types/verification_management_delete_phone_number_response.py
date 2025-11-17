# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["VerificationManagementDeletePhoneNumberResponse"]


class VerificationManagementDeletePhoneNumberResponse(BaseModel):
    phone_number: str
    """The E.164 formatted phone number that was removed from the list."""
