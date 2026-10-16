# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from .phone_verification_money import PhoneVerificationMoney

__all__ = ["HistoryListResponse", "Verification", "VerificationChannel"]


class VerificationChannel(BaseModel):
    channel: Literal["sms", "rcs", "whatsapp", "viber", "zalo", "telegram", "voice", "silent"]

    converted: bool
    """Whether the end user submitted a valid code received through this channel."""


class Verification(BaseModel):
    """One entry of the verification history.

    [Get a phone verification](/verify/v2/api-reference/history/get-a-phone-verification) returns the full record.
    """

    id: str
    """The verification identifier."""

    channels: List[VerificationChannel]
    """
    The channels the verification could use, and which one the end user converted
    through. Empty when the verification used only channels this API does not list.
    """

    created_at: datetime

    delivered: bool
    """Whether at least one message was reported delivered."""

    phone_number: str
    """The E.164 phone number the verification targeted."""

    status: Literal[
        "converted",
        "not_converted",
        "pending_check",
        "sent",
        "challenged",
        "suspected_fraud",
        "in_blocklist",
        "invalid_line",
        "invalid_number",
        "rate_limited",
        "expired_signals",
        "shadowed",
    ]
    """The outcome of the verification.

    - `converted` - The end user submitted a valid code.
    - `not_converted` - The verification expired without a valid code.
    - `pending_check` - A code was delivered and Prelude is still waiting for a
      check.
    - `sent` - A code was sent and the verification window is still open.
    - `challenged` - The verification was restricted to non-SMS and non-voice
      channels.
    - `suspected_fraud` - The anti-fraud system blocked the verification.
    - `in_blocklist` - The phone number is on the configured block list.
    - `invalid_line` - The phone number is not a valid line type.
    - `invalid_number` - The phone number is not a valid number.
    - `rate_limited` - The verification was refused by a rate limit.
    - `expired_signals` - The SDK signals were collected too long before the request
      to still attest to it.
    - `shadowed` - The anti-fraud system flagged the verification without blocking
      it.
    """

    attempts: Optional[int] = None
    """Number of messages sent for the verification, `0` when none was.

    Absent for sandboxed phone numbers.
    """

    converted_at: Optional[datetime] = None
    """When the end user submitted a valid code.

    Absent unless the verification converted.
    """

    cost: Optional[PhoneVerificationMoney] = None
    """Total cost of the verification. Absent when nothing was billed."""

    device_platform: Optional[Literal["android", "ios", "ipados", "tvos", "web"]] = None
    """Platform of the end-user device, when known."""

    phone_number_condition: Optional[Literal["allow_listed", "block_listed", "sandboxed"]] = None
    """
    Whether the phone number was allow-listed, block-listed, or sandboxed at
    verification time.
    """

    signals_hash_status: Optional[Literal["valid", "invalid"]] = None
    """Whether the SDK signals integrity check passed."""


class HistoryListResponse(BaseModel):
    verifications: List[Verification]
    """The page of verifications, most recent first."""

    next_cursor: Optional[str] = None
    """Pagination cursor for the next page of results.

    Omitted if there are no more pages.
    """
