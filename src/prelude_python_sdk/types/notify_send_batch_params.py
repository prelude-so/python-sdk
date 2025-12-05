# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["NotifySendBatchParams"]


class NotifySendBatchParams(TypedDict, total=False):
    template_id: Required[str]
    """The template identifier configured by your Customer Success team."""

    to: Required[SequenceNotStr[str]]
    """The list of recipients' phone numbers in E.164 format."""

    callback_url: str
    """The URL where webhooks will be sent for delivery events."""

    correlation_id: str
    """A user-defined identifier to correlate this request with your internal systems."""

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The message expiration date in RFC3339 format.

    Messages will not be sent after this time.
    """

    from_: Annotated[str, PropertyInfo(alias="from")]
    """The Sender ID. Must be approved for your account."""

    locale: str
    """A BCP-47 formatted locale string."""

    preferred_channel: Literal["sms", "whatsapp"]
    """Preferred channel for delivery. If unavailable, automatic fallback applies."""

    schedule_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Schedule delivery in RFC3339 format.

    Marketing sends may be adjusted to comply with local time windows.
    """

    variables: Dict[str, str]
    """The variables to be replaced in the template."""
