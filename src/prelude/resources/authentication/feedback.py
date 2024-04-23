# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)
from ...types.authentication import FeedbackCreateResponse, feedback_create_params

__all__ = ["Feedback", "AsyncFeedback"]


class Feedback(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FeedbackWithRawResponse:
        return FeedbackWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FeedbackWithStreamingResponse:
        return FeedbackWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_uuid: str,
        phone_number: str,
        status: Literal["onboarded", "not_onboarded"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackCreateResponse:
        """
        Send feedback

        Args:
          customer_uuid: Your customer UUID, which can be found in the API settings in the dashboard.

          phone_number: An E.164 formatted phone number.

          status: The type of the feedback.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/authentication/feedback",
            body=maybe_transform(
                {
                    "customer_uuid": customer_uuid,
                    "phone_number": phone_number,
                    "status": status,
                },
                feedback_create_params.FeedbackCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackCreateResponse,
        )


class AsyncFeedback(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFeedbackWithRawResponse:
        return AsyncFeedbackWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFeedbackWithStreamingResponse:
        return AsyncFeedbackWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_uuid: str,
        phone_number: str,
        status: Literal["onboarded", "not_onboarded"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FeedbackCreateResponse:
        """
        Send feedback

        Args:
          customer_uuid: Your customer UUID, which can be found in the API settings in the dashboard.

          phone_number: An E.164 formatted phone number.

          status: The type of the feedback.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/authentication/feedback",
            body=await async_maybe_transform(
                {
                    "customer_uuid": customer_uuid,
                    "phone_number": phone_number,
                    "status": status,
                },
                feedback_create_params.FeedbackCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FeedbackCreateResponse,
        )


class FeedbackWithRawResponse:
    def __init__(self, feedback: Feedback) -> None:
        self._feedback = feedback

        self.create = to_raw_response_wrapper(
            feedback.create,
        )


class AsyncFeedbackWithRawResponse:
    def __init__(self, feedback: AsyncFeedback) -> None:
        self._feedback = feedback

        self.create = async_to_raw_response_wrapper(
            feedback.create,
        )


class FeedbackWithStreamingResponse:
    def __init__(self, feedback: Feedback) -> None:
        self._feedback = feedback

        self.create = to_streamed_response_wrapper(
            feedback.create,
        )


class AsyncFeedbackWithStreamingResponse:
    def __init__(self, feedback: AsyncFeedback) -> None:
        self._feedback = feedback

        self.create = async_to_streamed_response_wrapper(
            feedback.create,
        )
