# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransactionalSendParams"]


class TransactionalSendParams(TypedDict, total=False):
    template_id: Required[str]
    """The template identifier."""

    to: Required[str]
    """The recipient's phone number."""

    callback_url: str
    """The callback URL."""

    correlation_id: str
    """A unique, user-defined identifier that will be included in webhook events."""

    expires_at: str
    """The message expiration date."""

    from_: Annotated[str, PropertyInfo(alias="from")]
    """The Sender ID."""

    variables: Dict[str, str]
    """The variables to be replaced in the template."""
