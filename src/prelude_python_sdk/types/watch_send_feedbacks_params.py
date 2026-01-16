# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WatchSendFeedbacksParams", "Feedback", "FeedbackTarget", "FeedbackMetadata", "FeedbackSignals"]


class WatchSendFeedbacksParams(TypedDict, total=False):
    feedbacks: Required[Iterable[Feedback]]
    """A list of feedbacks to send."""


class FeedbackTarget(TypedDict, total=False):
    """The feedback target. Only supports phone numbers for now."""

    type: Required[Literal["phone_number", "email_address"]]
    """The type of the target. Either "phone_number" or "email_address"."""

    value: Required[str]
    """An E.164 formatted phone number or an email address."""


class FeedbackMetadata(TypedDict, total=False):
    """The metadata for this feedback."""

    correlation_id: str
    """A user-defined identifier to correlate this feedback with.

    It is returned in the response and any webhook events that refer to this
    feedback.
    """


class FeedbackSignals(TypedDict, total=False):
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


class Feedback(TypedDict, total=False):
    target: Required[FeedbackTarget]
    """The feedback target. Only supports phone numbers for now."""

    type: Required[Literal["verification.started", "verification.completed"]]
    """The type of feedback."""

    dispatch_id: str
    """The identifier of the dispatch that came from the front-end SDK."""

    metadata: FeedbackMetadata
    """The metadata for this feedback."""

    signals: FeedbackSignals
    """The signals used for anti-fraud.

    For more details, refer to
    [Signals](/verify/v2/documentation/prevent-fraud#signals).
    """
