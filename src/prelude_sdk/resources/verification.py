# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import verification_check_params, verification_create_params
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
from ..types.verification_check_response import VerificationCheckResponse
from ..types.verification_create_response import VerificationCreateResponse

__all__ = ["VerificationResource", "AsyncVerificationResource"]


class VerificationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return VerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return VerificationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        target: verification_create_params.Target,
        metadata: verification_create_params.Metadata | NotGiven = NOT_GIVEN,
        options: verification_create_params.Options | NotGiven = NOT_GIVEN,
        signals: verification_create_params.Signals | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationCreateResponse:
        """Create a new verification for a specific phone number.

        If another non-expired
        verification exists (the request is performed within the verification window),
        this endpoint will perform a retry instead.

        Args:
          target: The target. Currently this can only be an E.164 formatted phone number.

          metadata: The metadata for this verification. This object will be returned with every
              response or webhook sent that refers to this verification.

          options: Verification options

          signals: The signals used for anti-fraud.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/verification",
            body=maybe_transform(
                {
                    "target": target,
                    "metadata": metadata,
                    "options": options,
                    "signals": signals,
                },
                verification_create_params.VerificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationCreateResponse,
        )

    def check(
        self,
        *,
        code: str,
        target: verification_check_params.Target,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationCheckResponse:
        """
        Check the validity of a verification code.

        Args:
          code: The OTP code to validate.

          target: The target. Currently this can only be an E.164 formatted phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/verification/check",
            body=maybe_transform(
                {
                    "code": code,
                    "target": target,
                },
                verification_check_params.VerificationCheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationCheckResponse,
        )


class AsyncVerificationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVerificationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncVerificationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerificationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return AsyncVerificationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        target: verification_create_params.Target,
        metadata: verification_create_params.Metadata | NotGiven = NOT_GIVEN,
        options: verification_create_params.Options | NotGiven = NOT_GIVEN,
        signals: verification_create_params.Signals | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationCreateResponse:
        """Create a new verification for a specific phone number.

        If another non-expired
        verification exists (the request is performed within the verification window),
        this endpoint will perform a retry instead.

        Args:
          target: The target. Currently this can only be an E.164 formatted phone number.

          metadata: The metadata for this verification. This object will be returned with every
              response or webhook sent that refers to this verification.

          options: Verification options

          signals: The signals used for anti-fraud.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/verification",
            body=await async_maybe_transform(
                {
                    "target": target,
                    "metadata": metadata,
                    "options": options,
                    "signals": signals,
                },
                verification_create_params.VerificationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationCreateResponse,
        )

    async def check(
        self,
        *,
        code: str,
        target: verification_check_params.Target,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VerificationCheckResponse:
        """
        Check the validity of a verification code.

        Args:
          code: The OTP code to validate.

          target: The target. Currently this can only be an E.164 formatted phone number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/verification/check",
            body=await async_maybe_transform(
                {
                    "code": code,
                    "target": target,
                },
                verification_check_params.VerificationCheckParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationCheckResponse,
        )


class VerificationResourceWithRawResponse:
    def __init__(self, verification: VerificationResource) -> None:
        self._verification = verification

        self.create = to_raw_response_wrapper(
            verification.create,
        )
        self.check = to_raw_response_wrapper(
            verification.check,
        )


class AsyncVerificationResourceWithRawResponse:
    def __init__(self, verification: AsyncVerificationResource) -> None:
        self._verification = verification

        self.create = async_to_raw_response_wrapper(
            verification.create,
        )
        self.check = async_to_raw_response_wrapper(
            verification.check,
        )


class VerificationResourceWithStreamingResponse:
    def __init__(self, verification: VerificationResource) -> None:
        self._verification = verification

        self.create = to_streamed_response_wrapper(
            verification.create,
        )
        self.check = to_streamed_response_wrapper(
            verification.check,
        )


class AsyncVerificationResourceWithStreamingResponse:
    def __init__(self, verification: AsyncVerificationResource) -> None:
        self._verification = verification

        self.create = async_to_streamed_response_wrapper(
            verification.create,
        )
        self.check = async_to_streamed_response_wrapper(
            verification.check,
        )
