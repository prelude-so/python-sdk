# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LookupLookupResponse", "NetworkInfo", "OriginalNetworkInfo"]


class NetworkInfo(BaseModel):
    carrier_name: Optional[str] = None
    """The name of the carrier."""

    mcc: Optional[str] = None
    """Mobile Country Code."""

    mnc: Optional[str] = None
    """Mobile Network Code."""


class OriginalNetworkInfo(BaseModel):
    carrier_name: Optional[str] = None
    """The name of the original carrier."""

    mcc: Optional[str] = None
    """Mobile Country Code."""

    mnc: Optional[str] = None
    """Mobile Network Code."""


class LookupLookupResponse(BaseModel):
    caller_name: Optional[str] = None
    """The CNAM (Caller ID Name) associated with the phone number.

    Contact us if you need to use this functionality. Once enabled, put `cnam`
    option to `type` query parameter.
    """

    country_code: Optional[str] = None
    """The country code of the phone number."""

    flags: Optional[List[Literal["ported", "temporary"]]] = None
    """A list of flags associated with the phone number.

    - `ported` - Indicates the phone number has been transferred from one carrier to
      another.
    - `temporary` - Indicates the phone number is likely a temporary or virtual
      number, often used for verification services or burner phones.
    """

    line_type: Optional[
        Literal[
            "calling_cards",
            "fixed_line",
            "isp",
            "local_rate",
            "mobile",
            "other",
            "pager",
            "payphone",
            "premium_rate",
            "satellite",
            "service",
            "shared_cost",
            "short_codes_commercial",
            "toll_free",
            "universal_access",
            "unknown",
            "vpn",
            "voice_mail",
            "voip",
        ]
    ] = None
    """The type of phone line.

    - `calling_cards` - Numbers that are associated with providers of pre-paid
      domestic and international calling cards.
    - `fixed_line` - Landline phone numbers.
    - `isp` - Numbers reserved for Internet Service Providers.
    - `local_rate` - Numbers that can be assigned non-geographically.
    - `mobile` - Mobile phone numbers.
    - `other` - Other types of services.
    - `pager` - Number ranges specifically allocated to paging devices.
    - `payphone` - Allocated numbers for payphone kiosks in some countries.
    - `premium_rate` - Landline numbers where the calling party pays more than
      standard.
    - `satellite` - Satellite phone numbers.
    - `service` - Automated applications.
    - `shared_cost` - Specific landline ranges where the cost of making the call is
      shared between the calling and called party.
    - `short_codes_commercial` - Short codes are memorable, easy-to-use numbers,
      like the UK's NHS 111, often sold to businesses. Not available in all
      countries.
    - `toll_free` - Number where the called party pays for the cost of the call not
      the calling party.
    - `universal_access` - Number ranges reserved for Universal Access initiatives.
    - `unknown` - Unknown phone number type.
    - `vpn` - Numbers are used exclusively within a private telecommunications
      network, connecting the operator's terminals internally and not accessible via
      the public telephone network.
    - `voice_mail` - A specific category of Interactive Voice Response (IVR)
      services.
    - `voip` - Specific ranges for providers of VoIP services to allow incoming
      calls from the regular telephony network.
    """

    network_info: Optional[NetworkInfo] = None
    """The current carrier information."""

    original_network_info: Optional[OriginalNetworkInfo] = None
    """The original carrier information."""

    phone_number: Optional[str] = None
    """The phone number."""
