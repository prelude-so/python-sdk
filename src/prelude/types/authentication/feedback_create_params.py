# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FeedbackCreateParams"]


class FeedbackCreateParams(TypedDict, total=False):
    customer_uuid: Required[str]
    """Your customer UUID, which can be found in the API settings in the dashboard."""

    phone_number: Required[str]
    """An E.164 formatted phone number."""

    status: Required[Literal["onboarded", "not_onboarded"]]
    """The type of the feedback."""
