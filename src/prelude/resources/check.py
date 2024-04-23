# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import CheckCreateResponse, check_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
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

__all__ = ["Check", "AsyncCheck"]


class Check(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CheckWithRawResponse:
        return CheckWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CheckWithStreamingResponse:
        return CheckWithStreamingResponse(self)

    def create(
        self,
        *,
        authentication_uuid: str,
        check_code: str,
        customer_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckCreateResponse:
        """
        Check a code

        Args:
          authentication_uuid: The authentication UUID that was returned when you created the authentication.

          check_code: The code that the user entered.

          customer_uuid: Your customer UUID, which can be found in the API settings in the Dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/check",
            body=maybe_transform(
                {
                    "authentication_uuid": authentication_uuid,
                    "check_code": check_code,
                    "customer_uuid": customer_uuid,
                },
                check_create_params.CheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckCreateResponse,
        )


class AsyncCheck(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCheckWithRawResponse:
        return AsyncCheckWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCheckWithStreamingResponse:
        return AsyncCheckWithStreamingResponse(self)

    async def create(
        self,
        *,
        authentication_uuid: str,
        check_code: str,
        customer_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CheckCreateResponse:
        """
        Check a code

        Args:
          authentication_uuid: The authentication UUID that was returned when you created the authentication.

          check_code: The code that the user entered.

          customer_uuid: Your customer UUID, which can be found in the API settings in the Dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/check",
            body=await async_maybe_transform(
                {
                    "authentication_uuid": authentication_uuid,
                    "check_code": check_code,
                    "customer_uuid": customer_uuid,
                },
                check_create_params.CheckCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CheckCreateResponse,
        )


class CheckWithRawResponse:
    def __init__(self, check: Check) -> None:
        self._check = check

        self.create = to_raw_response_wrapper(
            check.create,
        )


class AsyncCheckWithRawResponse:
    def __init__(self, check: AsyncCheck) -> None:
        self._check = check

        self.create = async_to_raw_response_wrapper(
            check.create,
        )


class CheckWithStreamingResponse:
    def __init__(self, check: Check) -> None:
        self._check = check

        self.create = to_streamed_response_wrapper(
            check.create,
        )


class AsyncCheckWithStreamingResponse:
    def __init__(self, check: AsyncCheck) -> None:
        self._check = check

        self.create = async_to_streamed_response_wrapper(
            check.create,
        )
