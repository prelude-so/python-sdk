# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WatchSendEventsParams", "Event", "EventTarget"]


class WatchSendEventsParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """A list of events to dispatch.

    A maximum of 100 events can be sent in a single request.
    """


class EventTarget(TypedDict, total=False):
    """The event target. Only supports phone numbers for now."""

    type: Required[Literal["phone_number", "email_address"]]
    """The type of the target. Either "phone_number" or "email_address"."""

    value: Required[str]
    """An E.164 formatted phone number or an email address."""


class Event(TypedDict, total=False):
    confidence: Required[Literal["maximum", "high", "neutral", "low", "minimum"]]
    """
    How much this event tells us to trust the end-user's legitimacy — not how
    certain you are that the event occurred. In increasing order of trust:
    `minimum`, `low`, `neutral`, `high`, `maximum`.

    Use `minimum` for an event tied to a user you trust the least to be legitimate
    (e.g. a `payment.chargeback`), and `maximum` for an event tied to a highly
    trustworthy user (e.g. a confirmed 3DS payment). Prelude weights these signals
    when scoring traffic: it filters out users tied to low-confidence events while
    preserving the experience for users tied to high-confidence ones.
    """

    label: Required[str]
    """A label to describe what the event refers to."""

    target: Required[EventTarget]
    """The event target. Only supports phone numbers for now."""
