# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["NotifyReplyResponse"]


class NotifyReplyResponse(BaseModel):
    id: str
    """The reply message identifier."""

    created_at: datetime
    """The reply creation date in RFC3339 format."""

    reply_to: str
    """The inbound message ID this reply was sent in response to."""

    text: str
    """The reply message body that was sent."""

    to: str
    """The recipient's phone number in E.164 format."""

    callback_url: Optional[str] = None
    """The callback URL where webhooks will be sent."""

    correlation_id: Optional[str] = None
    """The user-defined correlation identifier echoed back from the request."""
