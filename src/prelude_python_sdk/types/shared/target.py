# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Target"]


class Target(BaseModel):
    """The operation target. Either a phone number or an email address."""

    type: Literal["phone_number", "email_address"]
    """The type of the target. Either "phone_number" or "email_address"."""

    value: str
    """An E.164 formatted phone number or an email address."""
