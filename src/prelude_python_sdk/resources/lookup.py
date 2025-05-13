# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import lookup_lookup_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.lookup_lookup_response import LookupLookupResponse

__all__ = ["LookupResource", "AsyncLookupResource"]


class LookupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LookupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return LookupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LookupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return LookupResourceWithStreamingResponse(self)

    def lookup(
        self,
        phone_number: str,
        *,
        type: List[Literal["cnam"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LookupLookupResponse:
        """
        Retrieve detailed information about a phone number including carrier data, line
        type, and portability status.

        Args:
          phone_number: An E.164 formatted phone number to look up.

          type:
              Optional features. Possible values are:

              - `cnam` - Retrieve CNAM (Caller ID Name) along with other information. Contact
                us if you need to use this functionality.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            f"/v2/lookup/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"type": type}, lookup_lookup_params.LookupLookupParams),
            ),
            cast_to=LookupLookupResponse,
        )


class AsyncLookupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLookupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLookupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLookupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return AsyncLookupResourceWithStreamingResponse(self)

    async def lookup(
        self,
        phone_number: str,
        *,
        type: List[Literal["cnam"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LookupLookupResponse:
        """
        Retrieve detailed information about a phone number including carrier data, line
        type, and portability status.

        Args:
          phone_number: An E.164 formatted phone number to look up.

          type:
              Optional features. Possible values are:

              - `cnam` - Retrieve CNAM (Caller ID Name) along with other information. Contact
                us if you need to use this functionality.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            f"/v2/lookup/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"type": type}, lookup_lookup_params.LookupLookupParams),
            ),
            cast_to=LookupLookupResponse,
        )


class LookupResourceWithRawResponse:
    def __init__(self, lookup: LookupResource) -> None:
        self._lookup = lookup

        self.lookup = to_raw_response_wrapper(
            lookup.lookup,
        )


class AsyncLookupResourceWithRawResponse:
    def __init__(self, lookup: AsyncLookupResource) -> None:
        self._lookup = lookup

        self.lookup = async_to_raw_response_wrapper(
            lookup.lookup,
        )


class LookupResourceWithStreamingResponse:
    def __init__(self, lookup: LookupResource) -> None:
        self._lookup = lookup

        self.lookup = to_streamed_response_wrapper(
            lookup.lookup,
        )


class AsyncLookupResourceWithStreamingResponse:
    def __init__(self, lookup: AsyncLookupResource) -> None:
        self._lookup = lookup

        self.lookup = async_to_streamed_response_wrapper(
            lookup.lookup,
        )
