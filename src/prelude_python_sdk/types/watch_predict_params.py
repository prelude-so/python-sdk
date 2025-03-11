# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WatchPredictParams", "Target", "Signals"]


class WatchPredictParams(TypedDict, total=False):
    target: Required[Target]
    """The verification target.

    Either a phone number or an email address. To use the email verification feature
    contact us to discuss your use case.
    """

    signals: Signals
    """
    It is highly recommended that you provide the signals to increase prediction
    performance.
    """


class Target(TypedDict, total=False):
    type: Required[Literal["phone_number", "email_address"]]
    """The type of the target. Either "phone_number" or "email_address"."""

    value: Required[str]
    """An E.164 formatted phone number or an email address."""


class Signals(TypedDict, total=False):
    device_id: str
    """The unique identifier for the user's device.

    For Android, this corresponds to the `ANDROID_ID` and for iOS, this corresponds
    to the `identifierForVendor`.
    """

    device_model: str
    """The model of the user's device."""

    device_type: str
    """The type of the user's device."""

    ip: str
    """The IPv4 address of the user's device"""
