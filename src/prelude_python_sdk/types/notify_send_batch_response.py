# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["NotifySendBatchResponse", "Result", "ResultError", "ResultMessage"]


class ResultError(BaseModel):
    code: Optional[str] = None
    """The error code."""

    message: Optional[str] = None
    """A human-readable error message."""


class ResultMessage(BaseModel):
    id: Optional[str] = None
    """The message identifier."""

    correlation_id: Optional[str] = None
    """The correlation identifier for the message."""

    created_at: Optional[datetime] = None
    """The message creation date in RFC3339 format."""

    expires_at: Optional[datetime] = None
    """The message expiration date in RFC3339 format."""

    from_: Optional[str] = FieldInfo(alias="from", default=None)
    """The Sender ID used for this message."""

    locale: Optional[str] = None
    """The locale used for the message, if any."""

    schedule_at: Optional[datetime] = None
    """When the message will actually be sent in RFC3339 format with timezone offset."""

    to: Optional[str] = None
    """The recipient's phone number in E.164 format."""


class Result(BaseModel):
    phone_number: str
    """The recipient's phone number in E.164 format."""

    success: bool
    """Whether the message was accepted for delivery."""

    error: Optional[ResultError] = None
    """Present only if success is false."""

    message: Optional[ResultMessage] = None
    """Present only if success is true."""


class NotifySendBatchResponse(BaseModel):
    error_count: int
    """Number of failed sends."""

    results: List[Result]
    """The per-recipient result of the bulk send."""

    success_count: int
    """Number of successful sends."""

    total_count: int
    """Total number of recipients."""

    callback_url: Optional[str] = None
    """The callback URL used for this bulk request, if any."""

    request_id: Optional[str] = None
    """A string that identifies this specific request."""

    template_id: Optional[str] = None
    """The template identifier used for this bulk request."""

    variables: Optional[Dict[str, str]] = None
    """The variables used for this bulk request."""
