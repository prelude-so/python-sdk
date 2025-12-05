# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["NotifyListSubscriptionPhoneNumbersParams"]


class NotifyListSubscriptionPhoneNumbersParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor from the previous response"""

    limit: int
    """Maximum number of phone numbers to return per page"""

    state: Literal["SUB", "UNSUB"]
    """Filter by subscription state"""
