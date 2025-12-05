# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NotifyListSubscriptionPhoneNumberEventsParams"]


class NotifyListSubscriptionPhoneNumberEventsParams(TypedDict, total=False):
    config_id: Required[str]

    cursor: str
    """Pagination cursor from the previous response"""

    limit: int
    """Maximum number of events to return per page"""
