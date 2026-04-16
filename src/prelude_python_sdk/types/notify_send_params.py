# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NotifySendParams", "Context", "Document"]


class NotifySendParams(TypedDict, total=False):
    template_id: Required[str]
    """The template identifier configured by your Customer Success team."""

    to: Required[str]
    """The recipient's phone number in E.164 format."""

    callback_url: str
    """The URL where webhooks will be sent for message delivery events."""

    context: Context
    """Context for replying to an inbound message.

    When provided, the message is sent as a WhatsApp reply within the 24-hour
    conversation window.
    """

    correlation_id: str
    """A user-defined identifier to correlate this message with your internal systems.

    It is returned in the response and any webhook events that refer to this
    message.
    """

    document: Document
    """A document to attach to the message.

    Only supported on WhatsApp templates that have a document header.
    """

    expires_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The message expiration date in RFC3339 format.

    The message will not be sent if this time is reached.
    """

    from_: Annotated[str, PropertyInfo(alias="from")]
    """The Sender ID. Must be approved for your account."""

    locale: str
    """
    A BCP-47 formatted locale string with the language the text message will be sent
    to. If there's no locale set, the language will be determined by the country
    code of the phone number. If the language specified doesn't exist, the default
    set on the template will be used.
    """

    preferred_channel: Literal["sms", "rcs", "whatsapp"]
    """The preferred channel to be used in priority for message delivery.

    If the channel is unavailable, the system will fallback to other available
    channels.
    """

    schedule_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Schedule the message for future delivery in RFC3339 format.

    Marketing messages can be scheduled up to 90 days in advance and will be
    automatically adjusted for compliance with local time window restrictions.
    """

    text: str
    """The reply message body.

    Required when `context.reply_to` is provided. Used for 2-way WhatsApp messaging
    to send free-form text replies within a conversation window.
    """

    variables: Dict[str, str]
    """The variables to be replaced in the template."""


class Context(TypedDict, total=False):
    """Context for replying to an inbound message.

    When provided, the message is sent as a WhatsApp reply within the 24-hour conversation window.
    """

    reply_to: Required[str]
    """The inbound message ID (prefixed with `im_`) to reply to.

    This ID is provided in the `inbound.message.received` webhook event.
    """


class Document(TypedDict, total=False):
    """A document to attach to the message.

    Only supported on WhatsApp templates that have a document header.
    """

    filename: Required[str]
    """The filename to display for the document."""

    url: Required[str]
    """The URL of the document to attach. Must be a valid HTTP or HTTPS URL."""
