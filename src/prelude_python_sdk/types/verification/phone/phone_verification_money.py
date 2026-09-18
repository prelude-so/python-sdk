# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["PhoneVerificationMoney"]


class PhoneVerificationMoney(BaseModel):
    amount: str
    """Exact decimal amount.

    It is never rounded to the currency's minor units, so a sub-cent cost reads as
    `0.0004` rather than as `0.00`.
    """

    currency: str
    """ISO 4217 currency code."""
