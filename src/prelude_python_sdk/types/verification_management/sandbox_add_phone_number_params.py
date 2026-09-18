# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SandboxAddPhoneNumberParams"]


class SandboxAddPhoneNumberParams(TypedDict, total=False):
    attempt_code: Required[str]
    """
    The fixed attempt code that will validate verification attempts for this phone
    number.
    """

    phone_number: Required[str]
    """An E.164 formatted phone number to add to the sandbox list."""
