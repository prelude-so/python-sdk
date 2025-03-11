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
    """The verification target.

    Either a phone number or an email address. To use the email verification feature
    contact us to discuss your use case.
    """


class Feedback(TypedDict, total=False):
    type: Required[Literal["CONFIRM_TARGET"]]
    """
    `CONFIRM_TARGET` should be sent when you are sure that the user with this target
    (e.g. phone number) is trustworthy.
    """


class Target(TypedDict, total=False):
    type: Required[Literal["phone_number", "email_address"]]
    """The type of the target. Either "phone_number" or "email_address"."""

    value: Required[str]
    """An E.164 formatted phone number or an email address."""
