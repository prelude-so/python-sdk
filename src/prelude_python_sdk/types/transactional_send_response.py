# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TransactionalSendResponse"]


class TransactionalSendResponse(BaseModel):
    id: str
    """The message identifier."""

    created_at: datetime
    """The message creation date."""

    expires_at: datetime
    """The message expiration date."""

    template_id: str
    """The template identifier."""

    to: str
    """The recipient's phone number."""

    variables: Dict[str, str]
    """The variables to be replaced in the template."""

    callback_url: Optional[str] = None
    """The callback URL."""

    correlation_id: Optional[str] = None
    """A unique, user-defined identifier that will be included in webhook events."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The Sender ID."""
