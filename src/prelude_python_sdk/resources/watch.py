# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..types import watch_predict_params, watch_send_events_params, watch_send_feedbacks_params
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
from ..types.watch_predict_response import WatchPredictResponse
from ..types.watch_send_events_response import WatchSendEventsResponse
from ..types.watch_send_feedbacks_response import WatchSendFeedbacksResponse

__all__ = ["WatchResource", "AsyncWatchResource"]


class WatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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

    def predict(
        self,
        *,
        target: watch_predict_params.Target,
        dispatch_id: str | NotGiven = NOT_GIVEN,
        metadata: watch_predict_params.Metadata | NotGiven = NOT_GIVEN,
        signals: watch_predict_params.Signals | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchPredictResponse:
        """
        Predict the outcome of a verification based on Prelude’s anti-fraud system.

        Args:
          target: The prediction target. Only supports phone numbers for now.

          dispatch_id: The identifier of the dispatch that came from the front-end SDK.

          metadata: The metadata for this prediction.

          signals: The signals used for anti-fraud. For more details, refer to
              [Signals](/verify/v2/documentation/prevent-fraud#signals).

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
                    "dispatch_id": dispatch_id,
                    "metadata": metadata,
                    "signals": signals,
                },
                watch_predict_params.WatchPredictParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchPredictResponse,
        )

    def send_events(
        self,
        *,
        events: Iterable[watch_send_events_params.Event],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchSendEventsResponse:
        """
        Send real-time event data from end-user interactions within your application.
        Events will be analyzed for proactive fraud prevention and risk scoring.

        Args:
          events: A list of events to dispatch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/watch/event",
            body=maybe_transform({"events": events}, watch_send_events_params.WatchSendEventsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchSendEventsResponse,
        )

    def send_feedbacks(
        self,
        *,
        feedbacks: Iterable[watch_send_feedbacks_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchSendFeedbacksResponse:
        """Send feedback regarding your end-users verification funnel.

        Events will be
        analyzed for proactive fraud prevention and risk scoring.

        Args:
          feedbacks: A list of feedbacks to send.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/watch/feedback",
            body=maybe_transform({"feedbacks": feedbacks}, watch_send_feedbacks_params.WatchSendFeedbacksParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchSendFeedbacksResponse,
        )


class AsyncWatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
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

    async def predict(
        self,
        *,
        target: watch_predict_params.Target,
        dispatch_id: str | NotGiven = NOT_GIVEN,
        metadata: watch_predict_params.Metadata | NotGiven = NOT_GIVEN,
        signals: watch_predict_params.Signals | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchPredictResponse:
        """
        Predict the outcome of a verification based on Prelude’s anti-fraud system.

        Args:
          target: The prediction target. Only supports phone numbers for now.

          dispatch_id: The identifier of the dispatch that came from the front-end SDK.

          metadata: The metadata for this prediction.

          signals: The signals used for anti-fraud. For more details, refer to
              [Signals](/verify/v2/documentation/prevent-fraud#signals).

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
                    "dispatch_id": dispatch_id,
                    "metadata": metadata,
                    "signals": signals,
                },
                watch_predict_params.WatchPredictParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchPredictResponse,
        )

    async def send_events(
        self,
        *,
        events: Iterable[watch_send_events_params.Event],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchSendEventsResponse:
        """
        Send real-time event data from end-user interactions within your application.
        Events will be analyzed for proactive fraud prevention and risk scoring.

        Args:
          events: A list of events to dispatch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/watch/event",
            body=await async_maybe_transform({"events": events}, watch_send_events_params.WatchSendEventsParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchSendEventsResponse,
        )

    async def send_feedbacks(
        self,
        *,
        feedbacks: Iterable[watch_send_feedbacks_params.Feedback],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchSendFeedbacksResponse:
        """Send feedback regarding your end-users verification funnel.

        Events will be
        analyzed for proactive fraud prevention and risk scoring.

        Args:
          feedbacks: A list of feedbacks to send.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/watch/feedback",
            body=await async_maybe_transform(
                {"feedbacks": feedbacks}, watch_send_feedbacks_params.WatchSendFeedbacksParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchSendFeedbacksResponse,
        )


class WatchResourceWithRawResponse:
    def __init__(self, watch: WatchResource) -> None:
        self._watch = watch

        self.predict = to_raw_response_wrapper(
            watch.predict,
        )
        self.send_events = to_raw_response_wrapper(
            watch.send_events,
        )
        self.send_feedbacks = to_raw_response_wrapper(
            watch.send_feedbacks,
        )


class AsyncWatchResourceWithRawResponse:
    def __init__(self, watch: AsyncWatchResource) -> None:
        self._watch = watch

        self.predict = async_to_raw_response_wrapper(
            watch.predict,
        )
        self.send_events = async_to_raw_response_wrapper(
            watch.send_events,
        )
        self.send_feedbacks = async_to_raw_response_wrapper(
            watch.send_feedbacks,
        )


class WatchResourceWithStreamingResponse:
    def __init__(self, watch: WatchResource) -> None:
        self._watch = watch

        self.predict = to_streamed_response_wrapper(
            watch.predict,
        )
        self.send_events = to_streamed_response_wrapper(
            watch.send_events,
        )
        self.send_feedbacks = to_streamed_response_wrapper(
            watch.send_feedbacks,
        )


class AsyncWatchResourceWithStreamingResponse:
    def __init__(self, watch: AsyncWatchResource) -> None:
        self._watch = watch

        self.predict = async_to_streamed_response_wrapper(
            watch.predict,
        )
        self.send_events = async_to_streamed_response_wrapper(
            watch.send_events,
        )
        self.send_feedbacks = async_to_streamed_response_wrapper(
            watch.send_feedbacks,
        )
