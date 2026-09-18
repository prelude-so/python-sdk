# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .phone_verification_money import PhoneVerificationMoney

__all__ = ["PhoneVerificationPsd2Transaction"]


class PhoneVerificationPsd2Transaction(BaseModel):
    amount: Optional[PhoneVerificationMoney] = None

    recipient: Optional[str] = None
    """Payee name displayed to the payer."""
