# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import retry_create_params
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
from .._base_client import make_request_options
from ..types.retry_create_response import RetryCreateResponse

__all__ = ["RetryResource", "AsyncRetryResource"]


class RetryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prelude-python#accessing-raw-response-data-eg-headers
        """
        return RetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prelude-python#with_streaming_response
        """
        return RetryResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        authentication_uuid: str,
        customer_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetryCreateResponse:
        """
        Perform a retry

        Args:
          authentication_uuid: The authentication UUID that was returned when you created the authentication.

          customer_uuid: Your customer UUID, which can be found in the API settings in the dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/retry",
            body=maybe_transform(
                {
                    "authentication_uuid": authentication_uuid,
                    "customer_uuid": customer_uuid,
                },
                retry_create_params.RetryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetryCreateResponse,
        )


class AsyncRetryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prelude-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRetryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prelude-python#with_streaming_response
        """
        return AsyncRetryResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        authentication_uuid: str,
        customer_uuid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RetryCreateResponse:
        """
        Perform a retry

        Args:
          authentication_uuid: The authentication UUID that was returned when you created the authentication.

          customer_uuid: Your customer UUID, which can be found in the API settings in the dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/retry",
            body=await async_maybe_transform(
                {
                    "authentication_uuid": authentication_uuid,
                    "customer_uuid": customer_uuid,
                },
                retry_create_params.RetryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RetryCreateResponse,
        )


class RetryResourceWithRawResponse:
    def __init__(self, retry: RetryResource) -> None:
        self._retry = retry

        self.create = to_raw_response_wrapper(
            retry.create,
        )


class AsyncRetryResourceWithRawResponse:
    def __init__(self, retry: AsyncRetryResource) -> None:
        self._retry = retry

        self.create = async_to_raw_response_wrapper(
            retry.create,
        )


class RetryResourceWithStreamingResponse:
    def __init__(self, retry: RetryResource) -> None:
        self._retry = retry

        self.create = to_streamed_response_wrapper(
            retry.create,
        )


class AsyncRetryResourceWithStreamingResponse:
    def __init__(self, retry: AsyncRetryResource) -> None:
        self._retry = retry

        self.create = async_to_streamed_response_wrapper(
            retry.create,
        )
