# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WatchFeedbackParams", "Target", "Feedback"]


class WatchFeedbackParams(TypedDict, total=False):
    target: Required[Target]
    """The target. Currently this can only be an E.164 formatted phone number."""

    feedback: Feedback
    """
    You should send a feedback event back to Watch API when your user demonstrates
    authentic behaviour.
    """


class Target(TypedDict, total=False):
    type: Required[Literal["phone_number"]]
    """The type of the target. Currently this can only be "phone_number"."""

    value: Required[str]
    """An E.164 formatted phone number to verify."""


class Feedback(TypedDict, total=False):
    type: Literal["CONFIRM_PHONE_NUMBER"]
    """
    `CONFIRM_PHONE_NUMBER` should be sent when you are sure that the user with this
    phone number is trustworthy.
    """
