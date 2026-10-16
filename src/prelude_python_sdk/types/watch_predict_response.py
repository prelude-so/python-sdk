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
                "account_risk_profile",
                "automation_signature",
                "carrier_not_permitted",
                "client_fingerprint_mismatch",
                "custom_policy",
                "device_emulator",
                "device_not_permitted",
                "device_reuse",
                "expired_signals",
                "fraud_database",
                "invalid_signature",
                "ip_concentration",
                "ip_reputation",
                "location_mismatch",
                "missing_signals",
                "number_range_abuse",
                "poor_conversion_history",
                "proxy_network",
                "repeated_attempts",
                "temporary_phone_number",
            ]
        ]
    ] = None
    """The risk factors that contributed to the suspicious prediction.

    Only present when prediction is "suspicious" and the anti-fraud system detected
    specific risk signals.

    - `account_risk_profile` - The request matches a risk profile derived from the
      outcomes reported on your own account.
    - `automation_signature` - The request appears to come from an automated client
      rather than a person.
    - `carrier_not_permitted` - The destination carrier is one this account does not
      accept traffic for.
    - `client_fingerprint_mismatch` - The client does not appear to be the platform
      it identifies itself as.
    - `custom_policy` - A rule configured for your account matched this request.
    - `device_emulator` - The request appears to come from an emulator rather than a
      physical device.
    - `device_not_permitted` - The device platform is one your account blocks.
    - `device_reuse` - One device is driving verifications for an unusual number of
      phone numbers.
    - `expired_signals` - The SDK signals were collected too long before the request
      to still attest to it.
    - `fraud_database` - The phone number is flagged in one or more of the fraud
      databases Prelude consults.
    - `invalid_signature` - The SDK signature did not verify, so the request cannot
      be attributed to the device it claims to come from.
    - `ip_concentration` - The request shares its origin with an unusual volume of
      other verifications.
    - `ip_reputation` - The originating IP address is not trusted.
    - `location_mismatch` - The network location and the phone number's country are
      inconsistent.
    - `missing_signals` - The verification expected Prelude SDK signals and none
      arrived.
    - `number_range_abuse` - The phone number belongs to a range currently
      associated with abuse.
    - `poor_conversion_history` - Traffic resembling this request rarely completes a
      verification.
    - `proxy_network` - The request did not arrive over the subscriber's own access
      network.
    - `repeated_attempts` - The phone number exceeded the allowed number of
      verification attempts in a short period.
    - `temporary_phone_number` - The phone number belongs to a disposable or
      short-lived numbering service.
    """
