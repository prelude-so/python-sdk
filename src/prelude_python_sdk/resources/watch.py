# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..types import (
    watch_predict_params,
    watch_evaluate_params,
    watch_send_events_params,
    watch_send_feedbacks_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.shared_params.target import Target
from ..types.shared_params.signals import Signals
from ..types.watch_predict_response import WatchPredictResponse
from ..types.watch_evaluate_response import WatchEvaluateResponse
from ..types.watch_send_events_response import WatchSendEventsResponse
from ..types.watch_send_feedbacks_response import WatchSendFeedbacksResponse

__all__ = ["WatchResource", "AsyncWatchResource"]


class WatchResource(SyncAPIResource):
    """Evaluate email addresses and phone numbers for trustworthiness."""

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

    def evaluate(
        self,
        *,
        flow_id: str,
        target: Target,
        attributes: Dict[str, str] | Omit = omit,
        dispatch_id: str | Omit = omit,
        signals: Signals | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchEvaluateResponse:
        """**Beta.** The request and response shapes may still change.

        Talk to us before
        you build against it. Flows, recipes and rules are authored through the Watch
        Management API, or configured by Prelude on your behalf.

        Score a target against the rules configured for one moment in your product —
        signup, checkout, password reset. The flow selects which recipes run; each
        recipe scores its rules against a threshold and returns its own verdict, and the
        evaluation answers with the most severe verdict and action across them. Where
        Predict returns a single model-derived outcome, Eval returns the full breakdown,
        so you can see which rules fired and which could not run. Scoring-only — it does
        not update counters by itself.

        Args:
          flow_id: The flow to evaluate. A flow names the moment you are guarding and selects the
              recipes that run.

          target: The identifier to score — a phone number or email address.

          attributes: Values for the attributes the flow's recipes declare, keyed without the `attr.`
              namespace a rule uses to reference them.

              An attribute a recipe declares and this request omits is treated as missing
              evidence, not as an empty value: the rules reading it report `NOT_EVALUATED`
              rather than being scored as though the condition were false. A key no recipe in
              the flow declares is ignored rather than rejected, so one payload can serve
              flows that read different attributes.

          dispatch_id: The identifier of the dispatch that came from the front-end SDK. Signals it
              carries fill in anything the request did not state; the request wins where both
              supply a value.

          signals: The signals used for anti-fraud. For more details, refer to
              [Signals](/verify/v2/documentation/prevent-fraud#signals).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/watch/eval",
            body=maybe_transform(
                {
                    "flow_id": flow_id,
                    "target": target,
                    "attributes": attributes,
                    "dispatch_id": dispatch_id,
                    "signals": signals,
                },
                watch_evaluate_params.WatchEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchEvaluateResponse,
        )

    def predict(
        self,
        *,
        target: Target,
        dispatch_id: str | Omit = omit,
        metadata: watch_predict_params.Metadata | Omit = omit,
        signals: Signals | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchPredictResponse:
        """
        At signup, score the user's phone number or email address (target) as legitimate
        or suspicious. Scoring-only — does not update counters by itself. When using
        Feedback, call predict before verification.started on the same target (and
        correlation_id when used) so feedback can warm Watch auth-start counters. Use
        Events for product fraud labels; use Feedback only if you run your own phone
        verification funnel outside Prelude Verify.

        Args:
          target: The signup identifier to score — a phone number or email address.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchSendEventsResponse:
        """
        Send custom fraud signals from your application (labels and confidence levels).
        Events capture product-specific risk patterns and are weighted when scoring
        traffic. Use without Predict or Feedback if you only need to report product-side
        abuse (for example account.banned). Feedback is a separate, optional endpoint
        for self-hosted phone verification funnels.

        Args:
          events: A list of events to dispatch. A maximum of 100 events can be sent in a single
              request.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchSendFeedbacksResponse:
        """Optional.

        Report verification-funnel steps (verification.started,
        verification.completed) when you run phone verification outside Prelude Verify.
        Feeds Watch abuse-rate counters for your own flow. Call Predict on the same
        target before verification.started and reuse metadata.correlation_id so
        auth-start counters receive predict signals; without a linked predict, only
        attempt-rate counters update on started. Not required if you only use Events
        and/or Predict, or if Verify already handles verification for that traffic.

        Args:
          feedbacks: A list of feedbacks to send. A maximum of 100 feedbacks can be sent in a single
              request.

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
    """Evaluate email addresses and phone numbers for trustworthiness."""

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

    async def evaluate(
        self,
        *,
        flow_id: str,
        target: Target,
        attributes: Dict[str, str] | Omit = omit,
        dispatch_id: str | Omit = omit,
        signals: Signals | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchEvaluateResponse:
        """**Beta.** The request and response shapes may still change.

        Talk to us before
        you build against it. Flows, recipes and rules are authored through the Watch
        Management API, or configured by Prelude on your behalf.

        Score a target against the rules configured for one moment in your product —
        signup, checkout, password reset. The flow selects which recipes run; each
        recipe scores its rules against a threshold and returns its own verdict, and the
        evaluation answers with the most severe verdict and action across them. Where
        Predict returns a single model-derived outcome, Eval returns the full breakdown,
        so you can see which rules fired and which could not run. Scoring-only — it does
        not update counters by itself.

        Args:
          flow_id: The flow to evaluate. A flow names the moment you are guarding and selects the
              recipes that run.

          target: The identifier to score — a phone number or email address.

          attributes: Values for the attributes the flow's recipes declare, keyed without the `attr.`
              namespace a rule uses to reference them.

              An attribute a recipe declares and this request omits is treated as missing
              evidence, not as an empty value: the rules reading it report `NOT_EVALUATED`
              rather than being scored as though the condition were false. A key no recipe in
              the flow declares is ignored rather than rejected, so one payload can serve
              flows that read different attributes.

          dispatch_id: The identifier of the dispatch that came from the front-end SDK. Signals it
              carries fill in anything the request did not state; the request wins where both
              supply a value.

          signals: The signals used for anti-fraud. For more details, refer to
              [Signals](/verify/v2/documentation/prevent-fraud#signals).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/watch/eval",
            body=await async_maybe_transform(
                {
                    "flow_id": flow_id,
                    "target": target,
                    "attributes": attributes,
                    "dispatch_id": dispatch_id,
                    "signals": signals,
                },
                watch_evaluate_params.WatchEvaluateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WatchEvaluateResponse,
        )

    async def predict(
        self,
        *,
        target: Target,
        dispatch_id: str | Omit = omit,
        metadata: watch_predict_params.Metadata | Omit = omit,
        signals: Signals | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchPredictResponse:
        """
        At signup, score the user's phone number or email address (target) as legitimate
        or suspicious. Scoring-only — does not update counters by itself. When using
        Feedback, call predict before verification.started on the same target (and
        correlation_id when used) so feedback can warm Watch auth-start counters. Use
        Events for product fraud labels; use Feedback only if you run your own phone
        verification funnel outside Prelude Verify.

        Args:
          target: The signup identifier to score — a phone number or email address.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchSendEventsResponse:
        """
        Send custom fraud signals from your application (labels and confidence levels).
        Events capture product-specific risk patterns and are weighted when scoring
        traffic. Use without Predict or Feedback if you only need to report product-side
        abuse (for example account.banned). Feedback is a separate, optional endpoint
        for self-hosted phone verification funnels.

        Args:
          events: A list of events to dispatch. A maximum of 100 events can be sent in a single
              request.

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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WatchSendFeedbacksResponse:
        """Optional.

        Report verification-funnel steps (verification.started,
        verification.completed) when you run phone verification outside Prelude Verify.
        Feeds Watch abuse-rate counters for your own flow. Call Predict on the same
        target before verification.started and reuse metadata.correlation_id so
        auth-start counters receive predict signals; without a linked predict, only
        attempt-rate counters update on started. Not required if you only use Events
        and/or Predict, or if Verify already handles verification for that traffic.

        Args:
          feedbacks: A list of feedbacks to send. A maximum of 100 feedbacks can be sent in a single
              request.

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

        self.evaluate = to_raw_response_wrapper(
            watch.evaluate,
        )
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

        self.evaluate = async_to_raw_response_wrapper(
            watch.evaluate,
        )
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

        self.evaluate = to_streamed_response_wrapper(
            watch.evaluate,
        )
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

        self.evaluate = async_to_streamed_response_wrapper(
            watch.evaluate,
        )
        self.predict = async_to_streamed_response_wrapper(
            watch.predict,
        )
        self.send_events = async_to_streamed_response_wrapper(
            watch.send_events,
        )
        self.send_feedbacks = async_to_streamed_response_wrapper(
            watch.send_feedbacks,
        )
