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
    """Whether the user is a returning user on your app."""

    os_version: str
    """The version of the user's device operating system."""

    template_id: str
    """The template id associated with the message content variant to be sent."""
