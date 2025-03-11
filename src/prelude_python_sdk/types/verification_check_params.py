# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationCheckParams", "Target"]


class VerificationCheckParams(TypedDict, total=False):
    code: Required[str]
    """The OTP code to validate."""

    target: Required[Target]
    """The verification target.

    Either a phone number or an email address. To use the email verification feature
    contact us to discuss your use case.
    """


class Target(TypedDict, total=False):
    type: Required[Literal["phone_number", "email_address"]]
    """The type of the target. Either "phone_number" or "email_address"."""

    value: Required[str]
    """An E.164 formatted phone number or an email address."""
