# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["LookupLookupParams"]


class LookupLookupParams(TypedDict, total=False):
    type: List[Literal["cnam"]]
    """Optional features. Possible values are:

    - `cnam` - Retrieve CNAM (Caller ID Name) along with other information. Contact
      us if you need to use this functionality.
    """
