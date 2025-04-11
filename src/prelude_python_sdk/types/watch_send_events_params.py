# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WatchSendEventsParams", "Event", "EventTarget"]


class WatchSendEventsParams(TypedDict, total=False):
    events: Required[Iterable[Event]]
    """A list of events to dispatch."""


class EventTarget(TypedDict, total=False):
    type: Required[Literal["phone_number", "email_address"]]
    """The type of the target. Either "phone_number" or "email_address"."""

    value: Required[str]
    """An E.164 formatted phone number or an email address."""


class Event(TypedDict, total=False):
    confidence: Required[Literal["maximum", "high", "neutral", "low", "minimum"]]
    """A confidence level you want to assign to the event."""

    label: Required[str]
    """A label to describe what the event refers to."""

    target: Required[EventTarget]
    """The event target. Only supports phone numbers for now."""
