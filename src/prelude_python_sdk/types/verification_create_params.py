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
    """The verification target.

    Either a phone number or an email address. To use the email verification feature contact us to discuss your use case.
    """

    type: Required[Literal["phone_number", "email_address"]]
    """The type of the target. Either "phone_number" or "email_address"."""

    value: Required[str]
    """An E.164 formatted phone number or an email address."""


class Metadata(TypedDict, total=False):
    """The metadata for this verification.

    This object will be returned with every response or webhook sent that refers to this verification.
    """

    correlation_id: str
    """A user-defined identifier to correlate this verification with.

    It is returned in the response and any webhook events that refer to this
    verification.
    """


class OptionsAppRealm(TypedDict, total=False):
    """This allows automatic OTP retrieval on mobile apps and web browsers.

    Supported platforms are Android (SMS Retriever API) and Web (WebOTP API).
    """

    platform: Required[Literal["android", "web"]]
    """The platform for automatic OTP retrieval.

    Use "android" for the SMS Retriever API or "web" for the WebOTP API.
    """

    value: Required[str]
    """The value depends on the platform:

    - For Android: The SMS Retriever API hash code (11 characters). See
      [Google documentation](https://developers.google.com/identity/sms-retriever/verify#computing_your_apps_hash_string).
    - For Web: The origin domain (e.g., "example.com" or "www.example.com"). See
      [WebOTP API documentation](https://developer.mozilla.org/en-US/docs/Web/API/WebOTP_API).
    """


class Options(TypedDict, total=False):
    """Verification options"""

    app_realm: OptionsAppRealm
    """This allows automatic OTP retrieval on mobile apps and web browsers.

    Supported platforms are Android (SMS Retriever API) and Web (WebOTP API).
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

    method: Literal["auto", "voice", "message"]
    """The method used for verifying this phone number.

    The 'voice' option provides an accessible alternative for visually impaired
    users by delivering the verification code through a phone call rather than a
    text message. It also allows verification of landline numbers that cannot
    receive SMS messages. The 'message' option explicitly requests message delivery
    (SMS, WhatsApp ...) and skips silent verification, useful for scenarios
    requiring direct user interaction.
    """

    preferred_channel: Literal["sms", "rcs", "whatsapp", "viber", "zalo", "telegram"]
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
    """The signals used for anti-fraud.

    For more details, refer to [Signals](/verify/v2/documentation/prevent-fraud#signals).
    """

    app_version: str
    """The version of your application."""

    device_id: str
    """A unique ID for the user's device.

    You should ensure that each user device has a unique `device_id` value. Ideally,
    for Android, this corresponds to the `ANDROID_ID` and for iOS, this corresponds
    to the `identifierForVendor`.
    """

    device_model: str
    """The model of the user's device."""

    device_platform: Literal["android", "ios", "ipados", "tvos", "web"]
    """The type of the user's device."""

    ip: str
    """The public IP v4 or v6 address of the end-user's device.

    You should collect this from your backend. If your backend is behind a proxy,
    use the `X-Forwarded-For`, `Forwarded`, `True-Client-IP`, `CF-Connecting-IP` or
    an equivalent header to get the actual public IP of the end-user's device.
    """

    is_trusted_user: bool
    """
    This signal should indicate a higher level of trust, explicitly stating that the
    user is genuine. Contact us to discuss your use case. For more details, refer to
    [Signals](/verify/v2/documentation/prevent-fraud#signals).
    """

    ja4_fingerprint: str
    """The JA4 fingerprint observed for the end-user's connection.

    Prelude will infer it automatically when you use our Frontend SDKs (which use
    Prelude's edge network), but you can also forward the value if you terminate TLS
    yourself.
    """

    os_version: str
    """The version of the user's device operating system."""

    user_agent: str
    """The user agent of the user's device.

    If the individual fields (os_version, device_platform, device_model) are
    provided, we will prioritize those values instead of parsing them from the user
    agent string.
    """
