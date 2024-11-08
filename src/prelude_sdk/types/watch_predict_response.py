# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WatchPredictResponse", "Reasoning"]


class Reasoning(BaseModel):
    cause: Optional[Literal["none", "smart_antifraud", "repeat_number", "invalid_line"]] = None
    """A label explaining why the phone number was classified as not trustworthy"""

    score: Optional[float] = None
    """
    Indicates the risk of the phone number being genuine or involved in fraudulent
    patterns. The higher the riskier.
    """


class WatchPredictResponse(BaseModel):
    id: Optional[str] = None
    """A unique identifier for your prediction request."""

    prediction: Optional[Literal["allow", "block"]] = None
    """A label indicating the trustworthyness of the phone number."""

    reasoning: Optional[Reasoning] = None
