# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["NotifySendBatchParams", "Document"]


class NotifySendBatchParams(TypedDict, total=False):
    template_id: Required[str]
    """The template identifier configured by your Customer Success team."""

    to: Required[SequenceNotStr[str]]
    """The list of recipients' phone numbers in E.164 format."""

    callback_url: str
    """The URL where webhooks will be sent for delivery events."""

    correlation_id: str
    """A user-defined identifier to correlate this request with your internal systems."""

    document: Document
    """A media attachment to include in the message header.

    Supported on WhatsApp templates registered with a `DOCUMENT`, `IMAGE`, or
    `VIDEO` header. The media type is determined by the template's registered header
    format; send the matching file type for each.

    - `DOCUMENT` headers accept PDF and other document formats; `filename` is
      required and displayed to the recipient.
    - `IMAGE` headers accept `.png`, `.jpg`, `.jpeg`, and `.webp` URLs; `filename`
      is ignored.
    - `VIDEO` headers accept `.mp4` and `.3gp` URLs; `filename` is ignored.
    """

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The message expiration date in RFC3339 format.

    Messages will not be sent after this time.
    """

    from_: Annotated[str, PropertyInfo(alias="from")]
    """The Sender ID. Must be approved for your account."""

    locale: str
    """A BCP-47 formatted locale string."""

    preferred_channel: Literal["sms", "rcs", "whatsapp"]
    """Preferred channel for delivery. If unavailable, automatic fallback applies."""

    schedule_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Schedule delivery in RFC3339 format.

    Marketing sends may be adjusted to comply with local time windows.
    """

    variables: Dict[str, str]
    """The variables to be replaced in the template."""


class Document(TypedDict, total=False):
    """A media attachment to include in the message header.

    Supported on
    WhatsApp templates registered with a `DOCUMENT`, `IMAGE`, or
    `VIDEO` header. The media type is determined by the template's
    registered header format; send the matching file type for each.

    - `DOCUMENT` headers accept PDF and other document formats; `filename` is required and displayed to the recipient.
    - `IMAGE` headers accept `.png`, `.jpg`, `.jpeg`, and `.webp` URLs; `filename` is ignored.
    - `VIDEO` headers accept `.mp4` and `.3gp` URLs; `filename` is ignored.
    """

    url: Required[str]
    """HTTPS URL of the media file.

    The file extension must match the template's registered header format (PDF for
    DOCUMENT; PNG/JPG/JPEG/WEBP for IMAGE; MP4/3GP for VIDEO).
    """

    filename: str
    """Filename displayed to the recipient.

    Required for templates with a `DOCUMENT` header; ignored for `IMAGE` and `VIDEO`
    headers.
    """
