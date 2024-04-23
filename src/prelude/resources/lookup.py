# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import LookupRetrieveResponse
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)

__all__ = ["Lookup", "AsyncLookup"]


class Lookup(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LookupWithRawResponse:
        return LookupWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LookupWithStreamingResponse:
        return LookupWithStreamingResponse(self)

    def retrieve(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LookupRetrieveResponse:
        """
        Perform a phone number lookup

        Args:
          phone_number: An E.164 formatted phone number to look up.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            f"/lookup/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LookupRetrieveResponse,
        )


class AsyncLookup(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLookupWithRawResponse:
        return AsyncLookupWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLookupWithStreamingResponse:
        return AsyncLookupWithStreamingResponse(self)

    async def retrieve(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LookupRetrieveResponse:
        """
        Perform a phone number lookup

        Args:
          phone_number: An E.164 formatted phone number to look up.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            f"/lookup/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LookupRetrieveResponse,
        )


class LookupWithRawResponse:
    def __init__(self, lookup: Lookup) -> None:
        self._lookup = lookup

        self.retrieve = to_raw_response_wrapper(
            lookup.retrieve,
        )


class AsyncLookupWithRawResponse:
    def __init__(self, lookup: AsyncLookup) -> None:
        self._lookup = lookup

        self.retrieve = async_to_raw_response_wrapper(
            lookup.retrieve,
        )


class LookupWithStreamingResponse:
    def __init__(self, lookup: Lookup) -> None:
        self._lookup = lookup

        self.retrieve = to_streamed_response_wrapper(
            lookup.retrieve,
        )


class AsyncLookupWithStreamingResponse:
    def __init__(self, lookup: AsyncLookup) -> None:
        self._lookup = lookup

        self.retrieve = async_to_streamed_response_wrapper(
            lookup.retrieve,
        )
