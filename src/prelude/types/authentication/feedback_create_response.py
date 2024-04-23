# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["FeedbackCreateResponse"]


class FeedbackCreateResponse(BaseModel):
    uuid: Optional[str] = None
    """The UUID of the feedback."""
