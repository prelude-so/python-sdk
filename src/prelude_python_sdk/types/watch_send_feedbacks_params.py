# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WatchSendFeedbacksParams", "Feedback", "FeedbackTarget", "FeedbackMetadata", "FeedbackSignals"]


class WatchSendFeedbacksParams(TypedDict, total=False):
    feedbacks: Required[Iterable[Feedback]]
    """A list of feedbacks to send."""


class FeedbackTarget(TypedDict, total=False):
    type: Required[Literal["phone_number", "email_address"]]
    """The type of the target. Either "phone_number" or "email_address"."""

    value: Required[str]
    """An E.164 formatted phone number or an email address."""


class FeedbackMetadata(TypedDict, total=False):
    correlation_id: str
    """A user-defined identifier to correlate this feedback with."""


class FeedbackSignals(TypedDict, total=False):
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
