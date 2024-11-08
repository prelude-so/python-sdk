# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import transactional_send_params
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
from ..types.transactional_send_response import TransactionalSendResponse

__all__ = ["TransactionalResource", "AsyncTransactionalResource"]


class TransactionalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TransactionalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return TransactionalResourceWithStreamingResponse(self)

    def send(
        self,
        *,
        template_id: str,
        to: str,
        callback_url: str | NotGiven = NOT_GIVEN,
        correlation_id: str | NotGiven = NOT_GIVEN,
        expires_at: str | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        variables: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionalSendResponse:
        """
        Send a transactional message to your user.

        Args:
          template_id: The template identifier.

          to: The recipient's phone number.

          callback_url: The callback URL.

          correlation_id: A unique, user-defined identifier that will be included in webhook events.

          expires_at: The message expiration date.

          from_: The Sender ID.

          variables: The variables to be replaced in the template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/transactional",
            body=maybe_transform(
                {
                    "template_id": template_id,
                    "to": to,
                    "callback_url": callback_url,
                    "correlation_id": correlation_id,
                    "expires_at": expires_at,
                    "from_": from_,
                    "variables": variables,
                },
                transactional_send_params.TransactionalSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionalSendResponse,
        )


class AsyncTransactionalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransactionalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return AsyncTransactionalResourceWithStreamingResponse(self)

    async def send(
        self,
        *,
        template_id: str,
        to: str,
        callback_url: str | NotGiven = NOT_GIVEN,
        correlation_id: str | NotGiven = NOT_GIVEN,
        expires_at: str | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        variables: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TransactionalSendResponse:
        """
        Send a transactional message to your user.

        Args:
          template_id: The template identifier.

          to: The recipient's phone number.

          callback_url: The callback URL.

          correlation_id: A unique, user-defined identifier that will be included in webhook events.

          expires_at: The message expiration date.

          from_: The Sender ID.

          variables: The variables to be replaced in the template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/transactional",
            body=await async_maybe_transform(
                {
                    "template_id": template_id,
                    "to": to,
                    "callback_url": callback_url,
                    "correlation_id": correlation_id,
                    "expires_at": expires_at,
                    "from_": from_,
                    "variables": variables,
                },
                transactional_send_params.TransactionalSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TransactionalSendResponse,
        )


class TransactionalResourceWithRawResponse:
    def __init__(self, transactional: TransactionalResource) -> None:
        self._transactional = transactional

        self.send = to_raw_response_wrapper(
            transactional.send,
        )


class AsyncTransactionalResourceWithRawResponse:
    def __init__(self, transactional: AsyncTransactionalResource) -> None:
        self._transactional = transactional

        self.send = async_to_raw_response_wrapper(
            transactional.send,
        )


class TransactionalResourceWithStreamingResponse:
    def __init__(self, transactional: TransactionalResource) -> None:
        self._transactional = transactional

        self.send = to_streamed_response_wrapper(
            transactional.send,
        )


class AsyncTransactionalResourceWithStreamingResponse:
    def __init__(self, transactional: AsyncTransactionalResource) -> None:
        self._transactional = transactional

        self.send = async_to_streamed_response_wrapper(
            transactional.send,
        )
