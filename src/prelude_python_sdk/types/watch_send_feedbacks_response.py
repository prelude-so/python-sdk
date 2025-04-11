# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WatchSendFeedbacksResponse"]


class WatchSendFeedbacksResponse(BaseModel):
    request_id: str
    """A string that identifies this specific request.

    Report it back to us to help us diagnose your issues.
    """

    status: Literal["success"]
    """The status of the feedbacks sending."""
