# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["KYCMatchResponse"]


class KYCMatchResponse(BaseModel):
    """The per-attribute match result.

    Each `<attribute>_match` field is one of `true`, `false`, or `not_available` (the operator could not answer for that attribute). Fuzzy attributes additionally return a `<attribute>_match_score` (0-99 similarity) when they do not match exactly; the score is omitted on a match or when `not_available`.
    """

    address_match: Optional[Literal["true", "false", "not_available"]] = None
    """Whether the street address matched the operator's record."""

    address_match_score: Optional[int] = None
    """Similarity score (0-99) for the address. Returned only on a non-match."""

    birthdate_match: Optional[Literal["true", "false", "not_available"]] = None
    """Whether the date of birth matched the operator's record.

    Compared exactly; never scored.
    """

    country_code: Optional[str] = None
    """The country code of the phone number."""

    country_match: Optional[Literal["true", "false", "not_available"]] = None
    """Whether the country matched the operator's record.

    Compared exactly; never scored.
    """

    email_match: Optional[Literal["true", "false", "not_available"]] = None
    """Whether the email address matched the operator's record."""

    email_match_score: Optional[int] = None
    """Similarity score (0-99) for the email. Returned only on a non-match."""

    family_name_match: Optional[Literal["true", "false", "not_available"]] = None
    """Whether the family name matched the operator's record."""

    family_name_match_score: Optional[int] = None
    """Similarity score (0-99) for the family name. Returned only on a non-match."""

    given_name_match: Optional[Literal["true", "false", "not_available"]] = None
    """Whether the given name matched the operator's record."""

    given_name_match_score: Optional[int] = None
    """Similarity score (0-99) for the given name. Returned only on a non-match."""

    locality_match: Optional[Literal["true", "false", "not_available"]] = None
    """Whether the locality matched the operator's record."""

    locality_match_score: Optional[int] = None
    """Similarity score (0-99) for the locality. Returned only on a non-match."""

    operator: Optional[str] = None
    """The mobile operator that answered the match."""

    phone_number: Optional[str] = None
    """The phone number that was matched, in E.164 format."""

    postal_code_match: Optional[Literal["true", "false", "not_available"]] = None
    """Whether the postal code matched the operator's record.

    Compared exactly; never scored.
    """

    region_match: Optional[Literal["true", "false", "not_available"]] = None
    """Whether the region matched the operator's record."""

    region_match_score: Optional[int] = None
    """Similarity score (0-99) for the region. Returned only on a non-match."""

    request_id: Optional[str] = None
    """A string that identifies this specific request.

    Report it back to us to help us diagnose your issues.
    """
