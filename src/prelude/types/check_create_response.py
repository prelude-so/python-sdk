# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CheckCreateResponse"]


class CheckCreateResponse(BaseModel):
    authentication_uuid: Optional[str] = None
    """The UUID of the corresponding authentication."""

    status: Optional[
        Literal["unknown", "valid", "invalid", "without_attempt", "rate_limited", "already_validated", "expired_auth"]
    ] = None
    """The status of the check. Possible values are:

    - `unknown` - The status is unknown.
    - `valid` - The code is valid.
    - `invalid` - The code is invalid.
    - `without_attempt` - No attempt was sent yet, so a check cannot be completed.
    - `rate_limited` - The authentication was rate limited and cannot be checked.
    - `already_validated` - The authentication has already been validated.
    - `expired_auth` - The authentication has expired and cannot be checked.
    """
