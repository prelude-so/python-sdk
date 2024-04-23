# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AuthenticationCreateResponse"]


class AuthenticationCreateResponse(BaseModel):
    authentication_uuid: Optional[str] = None
    """
    A unique identifier for the authentication that you can use on the /check and
    /retry endpoints.
    """

    created_at: Optional[datetime] = None

    expires_at: Optional[datetime] = None
    """
    The time at which the authentication expires and can no longer be checked or
    retried.
    """

    status: Optional[Literal["pending", "rate_limited", "spam_detected"]] = None
    """The status of the authentication. Possible values are:

    - `pending` - The OTP code is being sent.
    - `rate_limited` - This user is rate-limited and cannot receive another code.
    - `spam_detected` - This attempt is flagged as spam. Go to the dashboard for
      more details.
    """
