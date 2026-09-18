# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .shared_params.target import Target
from .shared_params.signals import Signals

__all__ = ["WatchEvaluateParams"]


class WatchEvaluateParams(TypedDict, total=False):
    flow_id: Required[str]
    """The flow to evaluate.

    A flow names the moment you are guarding and selects the recipes that run.
    """

    target: Required[Target]
    """The identifier to score — a phone number or email address."""

    attributes: Dict[str, str]
    """
    Values for the attributes the flow's recipes declare, keyed without the `attr.`
    namespace a rule uses to reference them.

    An attribute a recipe declares and this request omits is treated as missing
    evidence, not as an empty value: the rules reading it report `NOT_EVALUATED`
    rather than being scored as though the condition were false. A key no recipe in
    the flow declares is ignored rather than rejected, so one payload can serve
    flows that read different attributes.
    """

    dispatch_id: str
    """The identifier of the dispatch that came from the front-end SDK.

    Signals it carries fill in anything the request did not state; the request wins
    where both supply a value.
    """

    signals: Signals
    """The signals used for anti-fraud.

    For more details, refer to
    [Signals](/verify/v2/documentation/prevent-fraud#signals).
    """
