# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["VerificationCheckParams", "Target"]


class VerificationCheckParams(TypedDict, total=False):
    target: Required[Target]
    """The target to verify.

    Currently this can only be an E.164 formatted phone number.
    """

    code: str
    """The OTP code to validate."""


class Target(TypedDict, total=False):
    type: Required[Literal["phone_number"]]
    """The type of the target to verify. Currently this can only be "phone_number"."""

    value: Required[str]
    """An E.164 formatted phone number to verify."""
