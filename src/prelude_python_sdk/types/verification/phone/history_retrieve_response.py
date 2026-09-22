# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from .phone_verification_money import PhoneVerificationMoney
from .phone_verification_carrier import PhoneVerificationCarrier
from .phone_verification_psd2_transaction import PhoneVerificationPsd2Transaction

__all__ = [
    "HistoryRetrieveResponse",
    "Lifecycle",
    "LifecycleEvent",
    "LifecycleEventAttempt",
    "LifecycleEventAttemptDeliveryEvent",
    "LifecycleEventCheck",
    "LifecycleEventCheckPsd2Info",
    "LifecycleEventCreate",
    "LifecycleEventSignals",
    "Signals",
]


class LifecycleEventAttemptDeliveryEvent(BaseModel):
    received_at: datetime

    status: Literal[
        "unknown",
        "submitted",
        "in_transit",
        "delivered",
        "undeliverable",
        "expired",
        "read",
        "silent_started",
        "silent_verified",
        "silent_mismatch",
    ]
    """The state this event reported.

    It is finer-grained than the attempt's `delivery_status` and includes the states
    a silent verification goes through.
    """


class LifecycleEventAttempt(BaseModel):
    """One message sent for this verification."""

    id: str

    created_at: datetime

    carrier: Optional[PhoneVerificationCarrier] = None
    """The end user's mobile network."""

    channel: Optional[Literal["sms", "rcs", "whatsapp", "viber", "zalo", "telegram", "voice", "silent"]] = None

    content: Optional[str] = None
    """Message body.

    While the verification can still be completed, the code inside it is masked
    rather than removed.
    """

    cost: Optional[PhoneVerificationMoney] = None

    delivery_events: Optional[List[LifecycleEventAttemptDeliveryEvent]] = None

    delivery_status: Optional[Literal["unknown", "in_transit", "delivered", "undeliverable", "read"]] = None

    preferred_channel: Optional[Literal["sms", "rcs", "whatsapp", "viber", "zalo", "telegram", "voice", "silent"]] = (
        None
    )
    """Channel you asked for, when it differs from the one used."""

    status: Optional[Literal["succeeded", "failed"]] = None

    trigger: Optional[Literal["initial", "auto_retry", "user_retry"]] = None
    """What caused the attempt."""


class LifecycleEventCheckPsd2Info(BaseModel):
    """Present on checks against a `prelude:psd2` code."""

    expected_transaction: Optional[PhoneVerificationPsd2Transaction] = None
    """The transaction submitted when the code was issued."""

    received_transaction: Optional[PhoneVerificationPsd2Transaction] = None
    """The transaction submitted with this check.

    Differs from `expected_transaction` when `status_detail` is
    `transaction_mismatch`.
    """


class LifecycleEventCheck(BaseModel):
    """One code submission for this verification."""

    created_at: datetime

    is_valid: bool

    channel: Optional[Literal["sms", "rcs", "whatsapp", "viber", "zalo", "telegram", "voice", "silent"]] = None

    psd2_info: Optional[LifecycleEventCheckPsd2Info] = None
    """Present on checks against a `prelude:psd2` code."""

    status_detail: Optional[
        Literal["expired_attempt", "expired_auth", "rate_limited", "transaction_missing", "transaction_mismatch"]
    ] = None
    """Why an invalid check failed, when known."""

    value: Optional[str] = None
    """The submitted code.

    Absent while the verification can still be completed, so that a check in flight
    cannot be read back through this endpoint, and absent on silent verification
    checks, which carry no code.
    """


class LifecycleEventCreate(BaseModel):
    created_at: datetime

    cost: Optional[PhoneVerificationMoney] = None


class LifecycleEventSignals(BaseModel):
    received_at: datetime

    expired_at: Optional[datetime] = None

    status: Optional[Literal["valid", "invalid"]] = None


class LifecycleEvent(BaseModel):
    """One timeline entry. `type` names the single payload field that is set."""

    type: Literal["create", "attempt", "check", "signals"]

    attempt: Optional[LifecycleEventAttempt] = None
    """One message sent for this verification."""

    check: Optional[LifecycleEventCheck] = None
    """One code submission for this verification."""

    create: Optional[LifecycleEventCreate] = None

    signals: Optional[LifecycleEventSignals] = None


class Lifecycle(BaseModel):
    """
    Chronological timeline of the verification: creation, message attempts with delivery events, code checks and signals reception. Omitted when Prelude holds no timeline for the verification.
    """

    events: List[LifecycleEvent]

    total_cost: Optional[PhoneVerificationMoney] = None

    undeliverable_route_count: Optional[int] = None
    """How many times the message was reported undeliverable by independent routes.

    Above zero usually means the phone number is incorrect or the device
    unreachable.
    """


class Signals(BaseModel):
    """The anti-fraud signals you forwarded when creating the verification."""

    is_trusted_user: bool
    """Whether you flagged this end user as trusted when creating the verification.

    Declared by you, not computed by Prelude.
    """

    device_id: Optional[str] = None
    """End-user device identifier you forwarded."""

    ja4_fingerprint: Optional[str] = None
    """TLS fingerprint you forwarded."""

    os_version: Optional[str] = None

    user_agent: Optional[str] = None


class HistoryRetrieveResponse(BaseModel):
    """A verification and everything Prelude recorded about it."""

    id: str
    """The verification identifier."""

    created_at: datetime

    expires_at: datetime

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

    app_version: Optional[str] = None
    """Version of your application, when known."""

    block_reasons: Optional[
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
    """Why the anti-fraud system blocked the verification.

    Empty unless it did. These are the same labels the Verify and Watch APIs serve
    as `risk_factors`.

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

    carrier: Optional[PhoneVerificationCarrier] = None
    """The end user's mobile network."""

    correlation_id: Optional[str] = None
    """The correlation identifier you supplied when creating the verification."""

    device_model: Optional[str] = None
    """Model of the end-user device, when known."""

    device_platform: Optional[Literal["android", "ios", "ipados", "tvos", "web"]] = None
    """Platform of the end-user device, when known."""

    ip_address: Optional[str] = None
    """IP address the verification was created from."""

    ip_address_region: Optional[str] = None
    """ISO 3166-1 alpha-2 region of the caller's IP address."""

    ip_distance_meters: Optional[int] = None
    """Distance between the phone number region and the IP location."""

    lifecycle: Optional[Lifecycle] = None
    """
    Chronological timeline of the verification: creation, message attempts with
    delivery events, code checks and signals reception. Omitted when Prelude holds
    no timeline for the verification.
    """

    phone_number_condition: Optional[Literal["allow_listed", "block_listed", "sandboxed"]] = None
    """
    Whether the phone number was allow-listed, block-listed, or sandboxed at
    verification time.
    """

    phone_number_current_condition: Optional[Literal["allow_listed", "block_listed", "sandboxed"]] = None
    """Whether the phone number is currently allow-listed, block-listed, or sandboxed."""

    phone_number_region: Optional[str] = None
    """ISO 3166-1 alpha-2 region of the phone number."""

    signals: Optional[Signals] = None
    """The anti-fraud signals you forwarded when creating the verification."""

    signals_hash_status: Optional[Literal["valid", "invalid"]] = None
    """Whether the SDK signals integrity check passed."""

    template_id: Optional[str] = None
    """The template used for this verification."""
