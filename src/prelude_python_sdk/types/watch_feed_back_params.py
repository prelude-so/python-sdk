# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WatchFeedBackParams", "Feedback", "Target"]


class WatchFeedBackParams(TypedDict, total=False):
    feedback: Required[Feedback]
    """
    You should send a feedback event back to Watch API when your user demonstrates
    authentic behavior.
    """

    target: Required[Target]
    """The target. Currently this can only be an E.164 formatted phone number."""


class Feedback(TypedDict, total=False):
    type: Required[Literal["CONFIRM_TARGET"]]
    """
    `CONFIRM_TARGET` should be sent when you are sure that the user with this target
    (e.g. phone number) is trustworthy.
    """


class Target(TypedDict, total=False):
    type: Required[Literal["phone_number"]]
    """The type of the target. Currently this can only be "phone_number"."""

    value: Required[str]
    """An E.164 formatted phone number to verify."""
