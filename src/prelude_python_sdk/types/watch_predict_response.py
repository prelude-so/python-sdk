# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WatchPredictResponse"]


class WatchPredictResponse(BaseModel):
    id: str
    """The prediction identifier."""

    prediction: Literal["legitimate", "suspicious"]
    """The prediction outcome."""

    request_id: str
    """A string that identifies this specific request.

    Report it back to us to help us diagnose your issues.
    """
