# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "AuthenticationRetrieveResponse",
    "Event",
    "EventAttempt",
    "EventCheck",
    "EventDeliveryStatus",
    "EventBalanceUpdate",
    "Signals",
]


class EventAttempt(BaseModel):
    id: Optional[str] = None
    """The ID of the attempt."""

    attempt_number: Optional[int] = None
    """The attempt number."""

    capability: Optional[Literal["rcs", "text", "whatsapp", "viber"]] = None
    """The capability of the attempt."""

    content: Optional[str] = None
    """The content of the attempt."""

    created_at: Optional[datetime] = None

    sender_id: Optional[str] = None
    """The sender ID of the attempt."""

    status: Optional[Literal["pending", "delivered", "failed", "rate_limited", "expired"]] = None
    """The status of the attempt. Possible values are:

    - `pending` - The attempt is pending.
    - `delivered` - The attempt was delivered.
    - `failed` - The attempt failed.
    - `rate_limited` - The authentication was rate limited and cannot be retried.
    - `expired` - The authentication has expired and cannot be retried.
    """

    type: Optional[Literal["attempt", "check", "delivery_status", "balance_update"]] = None
    """The type of the event."""


class EventCheck(BaseModel):
    id: Optional[str] = None
    """The ID of the check."""

    code: Optional[str] = None
    """The code that was checked."""

    created_at: Optional[datetime] = None

    status: Optional[
        Literal["unknown", "valid", "invalid", "without_attempt", "rate_limited", "already_validated", "expired_auth"]
    ] = None
    """The status of the check. Possible values are:

    - `unknown` - The status is unknown.
    - `valid` - The code is valid.
    - `invalid` - The code is invalid.
    - `without_attempt` - No attempt was sent yet, so a check cannot be completed.
    - `rate_limited` - The authentication was rate limited and cannot be checked.
    - `already_validated` - The authentication has already been validated.
    - `expired_auth` - The authentication has expired and cannot be checked.
    """

    type: Optional[Literal["attempt", "check", "delivery_status", "balance_update"]] = None
    """The type of the event."""


class EventDeliveryStatus(BaseModel):
    attempt_id: Optional[str] = None
    """The ID of the attempt."""

    attempt_number: Optional[int] = None
    """The attempt number."""

    created_at: Optional[datetime] = None

    originated_at: Optional[datetime] = None
    """The date and time from the provider."""

    status: Optional[Literal["unknown", "submitted", "in_transit", "delivered", "undeliverable"]] = None
    """The status of the delivery. Possible values are:

    - `unknown` - The status of the delivery is unknown.
    - `submitted` - The message has been submitted to the carrier.
    - `in_transit` - The message is in transit to the recipient.
    - `delivered` - The message has been delivered to the recipient.
    - `undeliverable` - The message could not be delivered to the recipient.
    """

    type: Optional[Literal["attempt", "check", "delivery_status", "balance_update"]] = None
    """The type of the event."""


class EventBalanceUpdate(BaseModel):
    amount: Optional[float] = None
    """The amount of the balance update."""

    balance_update_type: Optional[
        Literal[
            "unknown",
            "authentication",
            "attempt",
            "attempt_pending",
            "attempt_success",
            "authentication_pending",
            "authentication_success",
        ]
    ] = None

    created_at: Optional[datetime] = None

    type: Optional[Literal["attempt", "check", "delivery_status", "balance_update"]] = None
    """The type of the event."""


Event: TypeAlias = Union[EventAttempt, EventCheck, EventDeliveryStatus, EventBalanceUpdate]


class Signals(BaseModel):
    app_realm: Optional[str] = None
    """The Android SMS Retriever API hash code that identifies your app.

    This allows you to automatically retrieve and fill the OTP code on Android
    devices.
    """

    app_version: Optional[str] = None
    """The version of your application."""

    device_id: Optional[str] = None
    """Unique identifier for the user's device.

    For Android, this corresponds to the `ANDROID_ID` and for iOS, this corresponds
    to the `identifierForVendor`.
    """

    device_model: Optional[str] = None
    """The model of the user's device."""

    device_type: Optional[Literal["IOS", "ANDROID", "WEB"]] = None
    """The type of device the user is using."""

    ip: Optional[str] = None
    """The IP address of the user's device."""

    is_returning_user: Optional[bool] = None
    """
    This signal should do more than just confirm if a user is returning to your app;
    it should provide a higher level of trust, indicating that the user is genuine.
    For more details, refer to [Signals](/guides/prevent-fraud#signals).
    """

    os_version: Optional[str] = None
    """The version of the user's device operating system."""


class AuthenticationRetrieveResponse(BaseModel):
    correlation_id: Optional[str] = None
    """A unique, user-defined identifier that will be included in webhook events."""

    created_at: Optional[datetime] = None

    events: Optional[List[Event]] = None
    """Represents a collection of events that occur during the authentication process.

    Each event captures specific actions and outcomes related to the authentication
    attempts, checks, delivery statuses, and balance updates. The array can contain
    different types of events, each with its own structure and properties.
    """

    phone_number: Optional[str] = None
    """An E.164 formatted phone number."""

    signals: Optional[Signals] = None
    """
    [Signals](/guides/prevent-fraud#signals) are data points used to distinguish
    between fraudulent and legitimate users.
    """

    template_id: Optional[str] = None
    """The template id associated with the message content variant to be sent."""

    uuid: Optional[str] = None
    """The UUID of the corresponding authentication."""
