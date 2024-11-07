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
            "CallingCards",
            "FixedLine",
            "InternetServiceProvider",
            "LocalRate",
            "Mobile",
            "Other",
            "Pager",
            "PayPhone",
            "PremiumRate",
            "Satellite",
            "Service",
            "SharedCost",
            "ShortCodesCommercial",
            "TollFree",
            "UniversalAccess",
            "Unknown",
            "VPN",
            "VoiceMail",
            "Voip",
        ]
    ] = None
    """The type of phone line.

    - `CallingCards` - Numbers that are associated with providers of pre-paid
      domestic and international calling cards.
    - `FixedLine` - Landline phone numbers.
    - `InternetServiceProvider` - Numbers reserved for ISPs.
    - `LocalRate` - Numbers that can be assigned non-geographically.
    - `Mobile` - Mobile phone numbers.
    - `Other` - Other types of services.
    - `Pager` - Number ranges specifically allocated to paging devices.
    - `PayPhone` - Allocated numbers for payphone kiosks in some countries.
    - `PremiumRate` - Landline numbers where the calling party pays more than
      standard.
    - `Satellite` - Satellite phone numbers.
    - `Service` - Automated applications.
    - `SharedCost` - Specific landline ranges where the cost of making the call is
      shared between the calling and called party.
    - `ShortCodesCommercial` - Short codes are memorable, easy-to-use numbers, like
      the UK's NHS 111, often sold to businesses. Not available in all countries.
    - `TollFree` - Number where the called party pays for the cost of the call not
      the calling party.
    - `UniversalAccess` - Number ranges reserved for Universal Access initiatives.
    - `Unknown` - Unknown phone number type.
    - `VPN` - Numbers are used exclusively within a private telecommunications
      network, connecting the operator's terminals internally and not accessible via
      the public telephone network.
    - `VoiceMail` - A specific category of Interactive Voice Response (IVR)
      services.
    - `Voip` - Specific ranges for providers of VoIP services to allow incoming
      calls from the regular telephony network.
    """

    mcc: Optional[str] = None
    """The mobile country code of the phone number."""

    mnc: Optional[str] = None
    """The mobile network code of the phone number."""

    number_ported: Optional[bool] = None
    """Whether the phone number has been ported."""

    phone_number: Optional[str] = None
    """An E.164 formatted phone number."""
