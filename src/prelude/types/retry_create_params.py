# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RetryCreateParams"]


class RetryCreateParams(TypedDict, total=False):
    authentication_uuid: Required[str]
    """The authentication UUID that was returned when you created the authentication."""

    customer_uuid: Required[str]
    """Your customer UUID, which can be found in the API settings in the dashboard."""
