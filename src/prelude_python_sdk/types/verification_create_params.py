# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationCreateParams", "Target", "Metadata", "Options", "Signals"]


class VerificationCreateParams(TypedDict, total=False):
    target: Required[Target]
    """The target. Currently this can only be an E.164 formatted phone number."""

    metadata: Metadata
    """The metadata for this verification.

    This object will be returned with every response or webhook sent that refers to
    this verification.
    """

    options: Options
    """Verification options"""

    signals: Signals
    """The signals used for anti-fraud."""


class Target(TypedDict, total=False):
    type: Required[Literal["phone_number"]]
    """The type of the target. Currently this can only be "phone_number"."""

    value: Required[str]
    """An E.164 formatted phone number to verify."""


class Metadata(TypedDict, total=False):
    correlation_id: str
    """A user-defined identifier to correlate this verification with."""


class Options(TypedDict, total=False):
    app_realm: str
    """The Android SMS Retriever API hash code that identifies your app.

    This allows you to automatically retrieve and fill the OTP code on Android
    devices.
    """

    custom_code: str
    """The custom code to use for OTP verification.

    This feature is only available for compatibility purposes and subject to
    Prelude’s approval. Contact us to discuss your use case.
    """

    locale: str
    """
    A BCP-47 formatted locale string with the language the text message will be sent
    to. If there's no locale set, the language will be determined by the country
    code of the phone number. If the language specified doesn't exist, it defaults
    to US English.
    """

    sender_id: str
    """The Sender ID to use for this message.

    The Sender ID needs to be enabled by Prelude.
    """

    template_id: str
    """The identifier of a verification settings template.

    It is used to be able to switch behavior for specific use cases. Contact us if
    you need to use this functionality.
    """


class Signals(TypedDict, total=False):
    app_version: str
    """The version of your application."""

    device_id: str
    """The unique identifier for the user's device.

    For Android, this corresponds to the `ANDROID_ID` and for iOS, this corresponds
    to the `identifierForVendor`.
    """

    device_model: str
    """The model of the user's device."""

    device_platform: Literal["android", "ios", "ipados", "tvos", "web"]
    """The type of the user's device."""

    ip: str
    """The IP address of the user's device."""

    is_trusted_user: str
    """
    This signal should provide a higher level of trust, indicating that the user is
    genuine. For more details, refer to [Signals](/guides/prevent-fraud#signals).
    """

    os_version: str
    """The version of the user's device operating system."""
