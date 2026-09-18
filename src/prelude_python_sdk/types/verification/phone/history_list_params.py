# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["HistoryListParams"]


class HistoryListParams(TypedDict, total=False):
    channels: List[Literal["sms", "rcs", "whatsapp", "viber", "zalo", "telegram", "voice", "silent"]]
    """Only verifications that could use one of these channels.

    Repeat the parameter for several values.
    """

    cursor: str
    """Pagination cursor from the previous response."""

    device_platform: Literal["android", "ios", "ipados", "tvos", "web"]
    """Only verifications created from this device platform."""

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Only verifications created at or after this RFC 3339 timestamp.

    Goes with `to`, at most 6 months apart. Without them the whole history is
    searched.
    """

    limit: int
    """Maximum number of verifications to return per page."""

    max_attempts: int
    """Only verifications that sent at most this many messages.

    `0` keeps the verifications that never sent one.
    """

    min_attempts: int
    """Only verifications that sent at least this many messages."""

    phone_number: str
    """Only verifications targeting this E.164 phone number.

    The leading `+` may be omitted.
    """

    region: str
    """
    Only verifications of phone numbers from this region, as an ISO 3166-1 alpha-2
    code.
    """

    status: Literal[
        "converted",
        "not_converted",
        "pending_check",
        "sent",
        "challenged",
        "suspected_fraud",
        "in_blocklist",
        "invalid_line",
        "invalid_number",
        "rate_limited",
        "expired_signals",
        "shadowed",
    ]
    """Only verifications in this status. `pending_check` cannot be filtered on."""

    template_id: str
    """
    Only verifications sent with this template, as returned in `template_id` by
    [Get a phone verification](/verify/v2/api-reference/history/get-a-phone-verification).
    Built-in templates (`prelude:*`) cannot be filtered on.
    """

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only verifications created at or before this RFC 3339 timestamp.

    Goes with `from`.
    """
