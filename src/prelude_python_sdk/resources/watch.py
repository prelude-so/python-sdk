# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import watch_predict_params, watch_feed_back_params
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
from ..types.watch_predict_response import WatchPredictResponse
from ..types.watch_feed_back_response import WatchFeedBackResponse

__all__ = ["WatchResource", "AsyncWatchResource"]


class WatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return WatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return WatchResourceWithStreamingResponse(self)

    def feed_back(
        self,
        *,
        feedback: watch_feed_back_params.Feedback,
        target: watch_feed_back_params.Target,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchFeedBackResponse:
        """
        Once the user with a trustworthy phone number demonstrates authentic behavior,
        call this endpoint to report their authenticity to our systems.

        Args:
          feedback: You should send a feedback event back to Watch API when your user demonstrates
              authentic behavior.

          target: The target. Currently this can only be an E.164 formatted phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/watch/feedback",
            body=maybe_transform(
                {
                    "feedback": feedback,
                    "target": target,
                },
                watch_feed_back_params.WatchFeedBackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchFeedBackResponse,
        )

    def predict(
        self,
        *,
        target: watch_predict_params.Target,
        signals: watch_predict_params.Signals | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchPredictResponse:
        """
        Identify trustworthy phone numbers to mitigate fake traffic or traffic involved
        in fraud and international revenue share fraud (IRSF) patterns. This endpoint
        must be implemented in conjunction with the `watch/feedback` endpoint.

        Args:
          target: The target. Currently this can only be an E.164 formatted phone number.

          signals: It is highly recommended that you provide the signals to increase prediction
              performance.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/watch/predict",
            body=maybe_transform(
                {
                    "target": target,
                    "signals": signals,
                },
                watch_predict_params.WatchPredictParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchPredictResponse,
        )


class AsyncWatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return AsyncWatchResourceWithStreamingResponse(self)

    async def feed_back(
        self,
        *,
        feedback: watch_feed_back_params.Feedback,
        target: watch_feed_back_params.Target,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchFeedBackResponse:
        """
        Once the user with a trustworthy phone number demonstrates authentic behavior,
        call this endpoint to report their authenticity to our systems.

        Args:
          feedback: You should send a feedback event back to Watch API when your user demonstrates
              authentic behavior.

          target: The target. Currently this can only be an E.164 formatted phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/watch/feedback",
            body=await async_maybe_transform(
                {
                    "feedback": feedback,
                    "target": target,
                },
                watch_feed_back_params.WatchFeedBackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchFeedBackResponse,
        )

    async def predict(
        self,
        *,
        target: watch_predict_params.Target,
        signals: watch_predict_params.Signals | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchPredictResponse:
        """
        Identify trustworthy phone numbers to mitigate fake traffic or traffic involved
        in fraud and international revenue share fraud (IRSF) patterns. This endpoint
        must be implemented in conjunction with the `watch/feedback` endpoint.

        Args:
          target: The target. Currently this can only be an E.164 formatted phone number.

          signals: It is highly recommended that you provide the signals to increase prediction
              performance.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/watch/predict",
            body=await async_maybe_transform(
                {
                    "target": target,
                    "signals": signals,
                },
                watch_predict_params.WatchPredictParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchPredictResponse,
        )


class WatchResourceWithRawResponse:
    def __init__(self, watch: WatchResource) -> None:
        self._watch = watch

        self.feed_back = to_raw_response_wrapper(
            watch.feed_back,
        )
        self.predict = to_raw_response_wrapper(
            watch.predict,
        )


class AsyncWatchResourceWithRawResponse:
    def __init__(self, watch: AsyncWatchResource) -> None:
        self._watch = watch

        self.feed_back = async_to_raw_response_wrapper(
            watch.feed_back,
        )
        self.predict = async_to_raw_response_wrapper(
            watch.predict,
        )


class WatchResourceWithStreamingResponse:
    def __init__(self, watch: WatchResource) -> None:
        self._watch = watch

        self.feed_back = to_streamed_response_wrapper(
            watch.feed_back,
        )
        self.predict = to_streamed_response_wrapper(
            watch.predict,
        )


class AsyncWatchResourceWithStreamingResponse:
    def __init__(self, watch: AsyncWatchResource) -> None:
        self._watch = watch

        self.feed_back = async_to_streamed_response_wrapper(
            watch.feed_back,
        )
        self.predict = async_to_streamed_response_wrapper(
            watch.predict,
        )
