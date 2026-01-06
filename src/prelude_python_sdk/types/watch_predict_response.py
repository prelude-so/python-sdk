# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
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

    risk_factors: Optional[
        List[
            Literal[
                "behavioral_pattern",
                "device_attribute",
                "fraud_database",
                "location_discrepancy",
                "network_fingerprint",
                "poor_conversion_history",
                "prefix_concentration",
                "suspected_request_tampering",
                "suspicious_ip_address",
                "temporary_phone_number",
            ]
        ]
    ] = None
    """The risk factors that contributed to the suspicious prediction.

    Only present when prediction is "suspicious" and the anti-fraud system detected
    specific risk signals.

    - `behavioral_pattern` - The phone number past behavior during verification
      flows exhibits suspicious patterns.
    - `device_attribute` - The device exhibits characteristics associated with
      suspicious activity patterns.
    - `fraud_database` - The phone number has been flagged as suspicious in one or
      more of our fraud databases.
    - `location_discrepancy` - The phone number prefix and IP address discrepancy
      indicates potential fraud.
    - `network_fingerprint` - The network connection exhibits characteristics
      associated with suspicious activity patterns.
    - `poor_conversion_history` - The phone number has a history of poorly
      converting to a verified phone number.
    - `prefix_concentration` - The phone number is part of a range known to be
      associated with suspicious activity patterns.
    - `suspected_request_tampering` - The SDK signature is invalid and the request
      is considered to be tampered with.
    - `suspicious_ip_address` - The IP address is deemed to be associated with
      suspicious activity patterns.
    - `temporary_phone_number` - The phone number is known to be a temporary or
      disposable number.
    """
