# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VerificationCreateResponse", "Metadata", "Silent"]


class Metadata(BaseModel):
    """The metadata for this verification."""

    correlation_id: Optional[str] = None
    """A user-defined identifier to correlate this verification with.

    It is returned in the response and any webhook events that refer to this
    verification.
    """


class Silent(BaseModel):
    """The silent verification specific properties."""

    request_url: str
    """The URL to start the silent verification towards."""


class VerificationCreateResponse(BaseModel):
    id: str
    """The verification identifier."""

    method: Literal["email", "message", "silent", "voice"]
    """The method used for verifying this phone number."""

    status: Literal["success", "retry", "challenged", "blocked"]
    """The status of the verification.

    - `success` - A new verification window was created.
    - `retry` - A new attempt was created for an existing verification window.
    - `challenged` - The verification is suspicious and is restricted to non-SMS and
      non-voice channels only. This mode must be enabled for your customer account
      by Prelude support.
    - `blocked` - The verification was blocked.
    """

    channels: Optional[List[Literal["rcs", "silent", "sms", "telegram", "viber", "voice", "whatsapp", "zalo"]]] = None
    """The ordered sequence of channels to be used for verification"""

    metadata: Optional[Metadata] = None
    """The metadata for this verification."""

    reason: Optional[
        Literal[
            "expired_signature",
            "in_block_list",
            "invalid_phone_line",
            "invalid_phone_number",
            "invalid_signature",
            "repeated_attempts",
            "suspicious",
        ]
    ] = None
    """The reason why the verification was blocked.

    Only present when status is "blocked".

    - `expired_signature` - The signature of the SDK signals is expired. They should
      be sent within the hour following their collection.
    - `in_block_list` - The phone number is part of the configured block list.
    - `invalid_phone_line` - The phone number is not a valid line number (e.g.
      landline).
    - `invalid_phone_number` - The phone number is not a valid phone number (e.g.
      unallocated range).
    - `invalid_signature` - The signature of the SDK signals is invalid.
    - `repeated_attempts` - The phone number has made too many verification
      attempts.
    - `suspicious` - The verification attempt was deemed suspicious by the
      anti-fraud system.
    """

    request_id: Optional[str] = None

    risk_factors: Optional[
        List[
            Literal[
                "behavioral_pattern",
                "device_attribute",
                "fraud_database",
                "location_discrepancy",
                "network_fingerprint",
                "poor_conversion_history",
                "prefix_concentration",
                "suspected_request_tampering",
                "suspicious_ip_address",
                "temporary_phone_number",
            ]
        ]
    ] = None
    """The risk factors that contributed to the verification being blocked.

    Only present when status is "blocked" and the anti-fraud system detected
    specific risk signals.

    - `behavioral_pattern` - The phone number past behavior during verification
      flows exhibits suspicious patterns.
    - `device_attribute` - The device exhibits characteristics associated with
      suspicious activity patterns.
    - `fraud_database` - The phone number has been flagged as suspicious in one or
      more of our fraud databases.
    - `location_discrepancy` - The phone number prefix and IP address discrepancy
      indicates potential fraud.
    - `network_fingerprint` - The network connection exhibits characteristics
      associated with suspicious activity patterns.
    - `poor_conversion_history` - The phone number has a history of poorly
      converting to a verified phone number.
    - `prefix_concentration` - The phone number is part of a range known to be
      associated with suspicious activity patterns.
    - `suspected_request_tampering` - The SDK signature is invalid and the request
      is considered to be tampered with.
    - `suspicious_ip_address` - The IP address is deemed to be associated with
      suspicious activity patterns.
    - `temporary_phone_number` - The phone number is known to be a temporary or
      disposable number.
    """

    silent: Optional[Silent] = None
    """The silent verification specific properties."""
