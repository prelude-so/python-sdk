# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Signals"]


class Signals(BaseModel):
    """The signals used for anti-fraud.

    For more details, refer to [Signals](/verify/v2/documentation/prevent-fraud#signals).
    """

    app_version: Optional[str] = None
    """The version of your application."""

    device_id: Optional[str] = None
    """A unique ID for the user's device.

    You should ensure that each user device has a unique `device_id` value. Ideally,
    for Android, this corresponds to the `ANDROID_ID` and for iOS, this corresponds
    to the `identifierForVendor`.
    """

    device_model: Optional[str] = None
    """The model of the user's device."""

    device_platform: Optional[Literal["android", "ios", "ipados", "tvos", "web"]] = None
    """The type of the user's device."""

    existing_user: Optional[bool] = None
    """
    Whether the end-user already exists in your system, for example an existing
    account signing in again rather than a first-time signup. Unlike
    `is_trusted_user`, this signal does not bypass fraud checks; it is taken into
    account as one additional anti-fraud signal. For more details, refer to
    [Signals](/verify/v2/documentation/prevent-fraud#signals).
    """

    ip: Optional[str] = None
    """The public IP v4 or v6 address of the end-user's device.

    You should collect this from your backend. If your backend is behind a proxy,
    use the `X-Forwarded-For`, `Forwarded`, `True-Client-IP`, `CF-Connecting-IP` or
    an equivalent header to get the actual public IP of the end-user's device.
    """

    is_trusted_user: Optional[bool] = None
    """
    This signal should indicate a higher level of trust, explicitly stating that the
    user is genuine. Contact us to discuss your use case. For more details, refer to
    [Signals](/verify/v2/documentation/prevent-fraud#signals).
    """

    ja4_fingerprint: Optional[str] = None
    """The JA4 fingerprint observed for the end-user's connection.

    Prelude will infer it automatically when you use our Frontend SDKs (which use
    Prelude's edge network), but you can also forward the value if you terminate TLS
    yourself.
    """

    os_version: Optional[str] = None
    """The version of the user's device operating system."""

    user_agent: Optional[str] = None
    """The user agent of the user's device.

    If the individual fields (os_version, device_platform, device_model) are
    provided, we will prioritize those values instead of parsing them from the user
    agent string.
    """
