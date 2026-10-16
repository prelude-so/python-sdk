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

    status: Literal["success", "retry", "challenged", "blocked", "shadow_blocked"]
    """The status of the verification.

    - `success` - A new verification window was created.
    - `retry` - A new attempt was created for an existing verification window.
    - `challenged` - The verification is suspicious and is restricted to non-SMS and
      non-voice channels only. This mode must be enabled for your customer account
      by Prelude support.
    - `blocked` - The verification was blocked.
    - `shadow_blocked` - The verification triggered a block rule but the decision
      was not enforced; this is used to dry-run anti-fraud configuration. This mode
      must be enabled for your customer account by Prelude support.
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

    Only present when status is "blocked" or "shadow_blocked".

    - `expired_signature` - The signature of the SDK signals is expired. They should
      be sent within the hour following their collection.
    - `in_block_list` - The phone number is part of the configured block list.
    - `invalid_phone_line` - The phone number is not a valid line number (e.g.
      landline).
    - `invalid_phone_number` - The phone number is not a valid phone number (e.g.
      unallocated range).
    - `invalid_signature` - The SDK signature did not verify, so the request cannot
      be attributed to the device it claims to come from.
    - `repeated_attempts` - The phone number exceeded the allowed number of
      verification attempts in a short period.
    - `suspicious` - The verification attempt was deemed suspicious by the
      anti-fraud system.
    """

    request_id: Optional[str] = None

    risk_factors: Optional[
        List[
            Literal[
                "automation_signature",
                "carrier_not_permitted",
                "client_fingerprint_mismatch",
                "custom_policy",
                "device_emulator",
                "device_not_permitted",
                "device_reuse",
                "expired_signals",
                "fraud_database",
                "invalid_signature",
                "ip_concentration",
                "ip_reputation",
                "location_mismatch",
                "missing_signals",
                "number_range_abuse",
                "poor_conversion_history",
                "proxy_network",
                "repeated_attempts",
                "temporary_phone_number",
            ]
        ]
    ] = None
    """The risk factors that contributed to the verification being blocked.

    Only present when status is "blocked" or "shadow_blocked" and the anti-fraud
    system detected specific risk signals.

    - `automation_signature` - The request appears to come from an automated client
      rather than a person.
    - `carrier_not_permitted` - The destination carrier is one this account does not
      accept traffic for.
    - `client_fingerprint_mismatch` - The client does not appear to be the platform
      it identifies itself as.
    - `custom_policy` - A rule configured for your account matched this request.
    - `device_emulator` - The request appears to come from an emulator rather than a
      physical device.
    - `device_not_permitted` - The device platform is one your account blocks.
    - `device_reuse` - One device is driving verifications for an unusual number of
      phone numbers.
    - `expired_signals` - The SDK signals were collected too long before the request
      to still attest to it.
    - `fraud_database` - The phone number is flagged in one or more of the fraud
      databases Prelude consults.
    - `invalid_signature` - The SDK signature did not verify, so the request cannot
      be attributed to the device it claims to come from.
    - `ip_concentration` - The request shares its origin with an unusual volume of
      other verifications.
    - `ip_reputation` - The originating IP address is not trusted.
    - `location_mismatch` - The network location and the phone number's country are
      inconsistent.
    - `missing_signals` - The verification expected Prelude SDK signals and none
      arrived.
    - `number_range_abuse` - The phone number belongs to a range currently
      associated with abuse.
    - `poor_conversion_history` - Traffic resembling this request rarely completes a
      verification.
    - `proxy_network` - The request did not arrive over the subscriber's own access
      network.
    - `repeated_attempts` - The phone number exceeded the allowed number of
      verification attempts in a short period.
    - `temporary_phone_number` - The phone number belongs to a disposable or
      short-lived numbering service.
    """

    silent: Optional[Silent] = None
    """The silent verification specific properties."""
