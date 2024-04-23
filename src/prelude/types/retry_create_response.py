# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RetryCreateResponse"]


class RetryCreateResponse(BaseModel):
    authentication_uuid: Optional[str] = None
    """The UUID of the corresponding authentication."""

    created_at: Optional[datetime] = None

    next_retry_at: Optional[datetime] = None
    """The time at which the next retry will be available."""

    remaining_retry: Optional[int] = None
    """The number of remaining retries."""

    status: Optional[
        Literal["approved", "denied", "no_attempt", "rate_limited", "expired_auth", "already_validated"]
    ] = None
    """The status of the retry. Possible values are:

    - `approved` - The retry was approved and a new code was sent.
    - `denied` - The retry was denied.
    - `no_attempt` - No attempt was sent yet, so a retry cannot be completed.
    - `rate_limited` - The authentication was rate limited and cannot be retried.
    - `expired_auth` - The authentication has expired and cannot be retried.
    - `already_validated` - The authentication has already been validated.
    """
