# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VerificationManagementSubmitSenderIDParams"]


class VerificationManagementSubmitSenderIDParams(TypedDict, total=False):
    sender_id: Required[str]
    """The sender ID to add."""
