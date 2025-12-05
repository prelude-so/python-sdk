# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["NotifySendResponse"]


class NotifySendResponse(BaseModel):
    id: str
    """The message identifier."""

    created_at: datetime
    """The message creation date in RFC3339 format."""

    expires_at: datetime
    """The message expiration date in RFC3339 format."""

    template_id: str
    """The template identifier."""

    to: str
    """The recipient's phone number in E.164 format."""

    variables: Dict[str, str]
    """The variables to be replaced in the template."""

    callback_url: Optional[str] = None
    """The callback URL where webhooks will be sent."""

    correlation_id: Optional[str] = None
    """A user-defined identifier to correlate this message with your internal systems."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The Sender ID used for this message."""

    schedule_at: Optional[datetime] = None
    """When the message will actually be sent in RFC3339 format with timezone offset.

    For marketing messages, this may differ from the requested schedule_at due to
    automatic compliance adjustments.
    """
