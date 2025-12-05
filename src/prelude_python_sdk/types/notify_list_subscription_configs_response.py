# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["NotifyListSubscriptionConfigsResponse", "Config", "ConfigMessages", "ConfigMoPhoneNumber"]


class ConfigMessages(BaseModel):
    help_message: Optional[str] = None
    """Message sent when user requests help."""

    start_message: Optional[str] = None
    """Message sent when user subscribes."""

    stop_message: Optional[str] = None
    """Message sent when user unsubscribes."""


class ConfigMoPhoneNumber(BaseModel):
    country_code: str
    """The ISO 3166-1 alpha-2 country code."""

    phone_number: str
    """
    The phone number in E.164 format for long codes, or short code format for short
    codes.
    """


class Config(BaseModel):
    id: str
    """The subscription configuration ID."""

    callback_url: str
    """The URL to call when subscription status changes."""

    created_at: datetime
    """The date and time when the configuration was created."""

    messages: ConfigMessages
    """The subscription messages configuration."""

    name: str
    """The human-readable name for the subscription configuration."""

    updated_at: datetime
    """The date and time when the configuration was last updated."""

    mo_phone_numbers: Optional[List[ConfigMoPhoneNumber]] = None
    """A list of phone numbers for receiving inbound messages."""


class NotifyListSubscriptionConfigsResponse(BaseModel):
    configs: List[Config]
    """A list of subscription management configurations."""

    next_cursor: Optional[str] = None
    """Pagination cursor for the next page of results.

    Omitted if there are no more pages.
    """
