# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LookupRetrieveResponse"]


class LookupRetrieveResponse(BaseModel):
    carrier: Optional[str] = None
    """The carrier of the phone number."""

    country_code: Optional[str] = None
    """The ISO 3166-1 alpha-2 country code of the phone number."""

    line_type: Optional[
        Literal[
            "FixedLine",
            "Mobile",
            "TollFree",
            "PremiumRate",
            "SharedCost",
            "Voip",
            "Pager",
            "VoiceMail",
            "UniversalAccess",
            "Service",
            "Unknown",
        ]
    ] = None
    """The type of phone line."""

    mcc: Optional[str] = None
    """The mobile country code of the phone number."""

    mnc: Optional[str] = None
    """The mobile network code of the phone number."""

    number_ported: Optional[bool] = None
    """Whether the phone number has been ported."""

    phone_number: Optional[str] = None
    """An E.164 formatted phone number."""
