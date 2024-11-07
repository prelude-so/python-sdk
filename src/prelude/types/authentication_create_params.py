# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AuthenticationCreateParams"]


class AuthenticationCreateParams(TypedDict, total=False):
    customer_uuid: Required[str]
    """Your customer UUID, which can be found in the API settings in the dashboard."""

    phone_number: Required[str]
    """An E.164 formatted phone number to send the OTP to."""

    app_realm: str
    """The Android SMS Retriever API hash code that identifies your app.

    This allows you to automatically retrieve and fill the OTP code on Android
    devices.
    """

    app_version: str
    """The version of your application."""

    callback_url: str
    """A webhook URL to which delivery statuses will be sent."""

    correlation_id: str
    """A unique, user-defined identifier that will be included in webhook events"""

    device_id: str
    """Unique identifier for the user's device.

    For Android, this corresponds to the `ANDROID_ID` and for iOS, this corresponds
    to the `identifierForVendor`.
    """

    device_model: str
    """The model of the user's device."""

    device_type: Literal["IOS", "ANDROID", "WEB"]
    """The type of device the user is using."""

    ip: str
    """The IP address of the user's device."""

    is_returning_user: bool
    """
    This signal should do more than just confirm if a user is returning to your app;
    it should provide a higher level of trust, indicating that the user is genuine.
    For more details, refer to [Signals](/guides/prevent-fraud#signals).
    """

    locale: str
    """
    A BCP-47 locale indicating the language the SMS should be sent to; if this is
    not set, the SMS will be sent to the language specified by the country code of
    the message. If we don't support the language set, the message will be sent in
    US English (en-US).
    """

    os_version: str
    """The version of the user's device operating system."""

    sender_id: str
    """The Sender ID to use when sending the message."""

    template_id: str
    """The template id associated with the message content variant to be sent."""
