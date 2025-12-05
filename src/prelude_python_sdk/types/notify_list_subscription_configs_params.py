# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NotifyListSubscriptionConfigsParams"]


class NotifyListSubscriptionConfigsParams(TypedDict, total=False):
    cursor: str
    """Pagination cursor from the previous response"""

    limit: int
    """Maximum number of configurations to return per page"""
