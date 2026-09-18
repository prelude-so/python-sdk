# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["SandboxAddPhoneNumberResponse"]


class SandboxAddPhoneNumberResponse(BaseModel):
    attempt_code: str
    """The fixed attempt code associated with the sandbox phone number."""

    phone_number: str
    """The E.164 formatted phone number that was added to the sandbox list."""
