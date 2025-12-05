# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["NotifyGetSubscriptionConfigResponse", "Messages", "MoPhoneNumber"]


class Messages(BaseModel):
    help_message: Optional[str] = None
    """Message sent when user requests help."""

    start_message: Optional[str] = None
    """Message sent when user subscribes."""

    stop_message: Optional[str] = None
    """Message sent when user unsubscribes."""


class MoPhoneNumber(BaseModel):
    country_code: str
    """The ISO 3166-1 alpha-2 country code."""

    phone_number: str
    """
    The phone number in E.164 format for long codes, or short code format for short
    codes.
    """


class NotifyGetSubscriptionConfigResponse(BaseModel):
    id: str
    """The subscription configuration ID."""

    callback_url: str
    """The URL to call when subscription status changes."""

    created_at: datetime
    """The date and time when the configuration was created."""

    messages: Messages
    """The subscription messages configuration."""

    name: str
    """The human-readable name for the subscription configuration."""

    updated_at: datetime
    """The date and time when the configuration was last updated."""

    mo_phone_numbers: Optional[List[MoPhoneNumber]] = None
    """A list of phone numbers for receiving inbound messages."""
