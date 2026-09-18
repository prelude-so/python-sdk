# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NotifyReplyParams"]


class NotifyReplyParams(TypedDict, total=False):
    reply_to: Required[str]
    """The inbound message ID (prefixed with `im_`) to reply to.

    This ID is provided in the `inbound.message.received` webhook event.
    """

    text: Required[str]
    """The reply message body sent as a free-form WhatsApp text."""

    to: Required[str]
    """The recipient's phone number in E.164 format.

    Must match the phone number that sent the original inbound message.
    """

    callback_url: str
    """The URL where webhooks will be sent for delivery events of this reply."""

    correlation_id: str
    """A user-defined identifier to correlate this reply with your internal systems.

    It is returned in the response and any webhook events that refer to this
    message.
    """
