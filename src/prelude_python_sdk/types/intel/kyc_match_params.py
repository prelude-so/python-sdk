# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["KYCMatchParams"]


class KYCMatchParams(TypedDict, total=False):
    address: str
    """The street address."""

    birthdate: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
    """The date of birth in ISO 8601 (`YYYY-MM-DD`) format. Compared exactly."""

    country: str
    """The ISO 3166-1 alpha-2 country code. Compared exactly."""

    email: str
    """The email address."""

    family_name: str
    """The end-user's family (last) name."""

    given_name: str
    """The end-user's given (first) name."""

    locality: str
    """The locality (city)."""

    postal_code: str
    """The postal code. Compared exactly."""

    region: str
    """The region, state, or province."""
