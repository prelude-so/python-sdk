# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.target import Target
from .shared_params.signals import Signals

__all__ = ["WatchPredictParams", "Metadata"]


class WatchPredictParams(TypedDict, total=False):
    target: Required[Target]
    """The signup identifier to score — a phone number or email address."""

    dispatch_id: str
    """The identifier of the dispatch that came from the front-end SDK."""

    metadata: Metadata
    """The metadata for this prediction."""

    signals: Signals
    """The signals used for anti-fraud.

    For more details, refer to
    [Signals](/verify/v2/documentation/prevent-fraud#signals).
    """


class Metadata(TypedDict, total=False):
    """The metadata for this prediction."""

    correlation_id: str
    """A user-defined identifier to correlate this prediction with.

    It is returned in the response and any webhook events that refer to this
    prediction.
    """
