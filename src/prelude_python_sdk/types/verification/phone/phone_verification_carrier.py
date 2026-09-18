# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["PhoneVerificationCarrier"]


class PhoneVerificationCarrier(BaseModel):
    """The end user's mobile network."""

    mccmnc: str

    name: Optional[str] = None
