# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationCreateParams", "Target", "Metadata", "Options", "OptionsAppRealm", "Signals"]


class VerificationCreateParams(TypedDict, total=False):
    target: Required[Target]
    """The verification target.

    Either a phone number or an email address. To use the email verification feature
    contact us to discuss your use case.
    """

    dispatch_id: str
    """The identifier of the dispatch that came from the front-end SDK."""

    metadata: Metadata
    """The metadata for this verification.

    This object will be returned with every response or webhook sent that refers to
    this verification.
    """

    options: Options
    """Verification options"""

    signals: Signals
    """The signals used for anti-fraud.

    For more details, refer to
    [Signals](/verify/v2/documentation/prevent-fraud#signals).
    """


class Target(TypedDict, total=False):
    type: Required[Literal["phone_number", "email_address"]]
    """The type of the target. Either "phone_number" or "email_address"."""

    value: Required[str]
    """An E.164 formatted phone number or an email address."""


class Metadata(TypedDict, total=False):
    correlation_id: str
    """A user-defined identifier to correlate this verification with."""


class OptionsAppRealm(TypedDict, total=False):
    platform: Required[Literal["android"]]
    """The platform the SMS will be sent to.

    We are currently only supporting "android".
    """

    value: Required[str]
    """The Android SMS Retriever API hash code that identifies your app."""


class Options(TypedDict, total=False):
    app_realm: OptionsAppRealm
    """This allows you to automatically retrieve and fill the OTP code on mobile apps.

    Currently only Android devices are supported.
    """

    callback_url: str
    """
    The URL where webhooks will be sent when verification events occur, including
    verification creation, attempt creation, and delivery status changes. For more
    details, refer to [Webhook](/verify/v2/documentation/webhook).
    """

    code_size: int
    """The size of the code generated.

    It should be between 4 and 8. Defaults to the code size specified from the
    Dashboard.
    """

    custom_code: str
    """The custom code to use for OTP verification.

    To use the custom code feature, contact us to enable it for your account. For
    more details, refer to [Custom Code](/verify/v2/documentation/custom-codes).
    """

    locale: str
    """
    A BCP-47 formatted locale string with the language the text message will be sent
    to. If there's no locale set, the language will be determined by the country
    code of the phone number. If the language specified doesn't exist, it defaults
    to US English.
    """

    method: Literal["auto", "voice"]
    """The method used for verifying this phone number.

    The 'voice' option provides an accessible alternative for visually impaired
    users by delivering the verification code through a phone call rather than a
    text message. It also allows verification of landline numbers that cannot
    receive SMS messages.
    """

    preferred_channel: Literal["sms", "rcs", "whatsapp", "viber", "zalo", "telegram", "silent", "voice"]
    """The preferred channel to be used in priority for verification."""

    sender_id: str
    """The Sender ID to use for this message.

    The Sender ID needs to be enabled by Prelude.
    """

    template_id: str
    """The identifier of a verification template.

    It applies use case-specific settings, such as the message content or certain
    verification parameters.
    """

    variables: Dict[str, str]
    """The variables to be replaced in the template."""


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

    is_trusted_user: bool
    """
    This signal should provide a higher level of trust, indicating that the user is
    genuine. Contact us to discuss your use case. For more details, refer to
    [Signals](/verify/v2/documentation/prevent-fraud#signals).
    """

    os_version: str
    """The version of the user's device operating system."""

    user_agent: str
    """The user agent of the user's device.

    If the individual fields (os_version, device_platform, device_model) are
    provided, we will prioritize those values instead of parsing them from the user
    agent string.
    """
