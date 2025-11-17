# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VerificationManagementSetPhoneNumberParams"]


class VerificationManagementSetPhoneNumberParams(TypedDict, total=False):
    phone_number: Required[str]
    """An E.164 formatted phone number to add to the list."""
