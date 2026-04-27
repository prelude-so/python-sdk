# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WatchSendFeedbacksParams", "Feedback", "FeedbackTarget", "FeedbackMetadata"]


class WatchSendFeedbacksParams(TypedDict, total=False):
    feedbacks: Required[Iterable[Feedback]]
    """A list of feedbacks to send.

    A maximum of 100 feedbacks can be sent in a single request.
    """


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


class Feedback(TypedDict, total=False):
    target: Required[FeedbackTarget]
    """The feedback target. Only supports phone numbers for now."""

    type: Required[Literal["verification.started", "verification.completed"]]
    """The type of feedback."""

    metadata: FeedbackMetadata
    """The metadata for this feedback."""
