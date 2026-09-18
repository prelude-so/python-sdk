# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.verification_management import sandbox_add_phone_number_params
from ...types.verification_management.sandbox_add_phone_number_response import SandboxAddPhoneNumberResponse
from ...types.verification_management.sandbox_list_phone_numbers_response import SandboxListPhoneNumbersResponse
from ...types.verification_management.sandbox_delete_phone_number_response import SandboxDeletePhoneNumberResponse

__all__ = ["SandboxResource", "AsyncSandboxResource"]


class SandboxResource(SyncAPIResource):
    """Verify phone numbers."""

    @cached_property
    def with_raw_response(self) -> SandboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return SandboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SandboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return SandboxResourceWithStreamingResponse(self)

    def add_phone_number(
        self,
        *,
        attempt_code: str,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxAddPhoneNumberResponse:
        """
        Register a phone number as a sandbox number and associate it with a fixed
        attempt code. Subsequent verification attempts against this number will not
        trigger a real SMS/call and will validate against the configured attempt code.

        This operation is idempotent - re-adding the same phone number will overwrite
        the existing attempt code.

        In order to get access to this endpoint, contact our support team.

        Args:
          attempt_code: The fixed attempt code that will validate verification attempts for this phone
              number.

          phone_number: An E.164 formatted phone number to add to the sandbox list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v2/verification/management/phone-numbers/sandbox",
            body=maybe_transform(
                {
                    "attempt_code": attempt_code,
                    "phone_number": phone_number,
                },
                sandbox_add_phone_number_params.SandboxAddPhoneNumberParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxAddPhoneNumberResponse,
        )

    def delete_phone_number(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxDeletePhoneNumberResponse:
        """
        Remove a phone number from the sandbox list.

        This operation is idempotent - deleting a phone number that is not in the
        sandbox list will succeed without making any changes.

        In order to get access to this endpoint, contact our support team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._delete(
            path_template(
                "/v2/verification/management/phone-numbers/sandbox/{phone_number}", phone_number=phone_number
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxDeletePhoneNumberResponse,
        )

    def list_phone_numbers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxListPhoneNumbersResponse:
        """Retrieve the list of sandbox phone numbers for the account.

        Sandbox numbers are
        test numbers that bypass the real verification flow and return a fixed attempt
        code.

        In order to get access to this endpoint, contact our support team.
        """
        return self._get(
            "/v2/verification/management/phone-numbers/sandbox",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxListPhoneNumbersResponse,
        )


class AsyncSandboxResource(AsyncAPIResource):
    """Verify phone numbers."""

    @cached_property
    def with_raw_response(self) -> AsyncSandboxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSandboxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSandboxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return AsyncSandboxResourceWithStreamingResponse(self)

    async def add_phone_number(
        self,
        *,
        attempt_code: str,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxAddPhoneNumberResponse:
        """
        Register a phone number as a sandbox number and associate it with a fixed
        attempt code. Subsequent verification attempts against this number will not
        trigger a real SMS/call and will validate against the configured attempt code.

        This operation is idempotent - re-adding the same phone number will overwrite
        the existing attempt code.

        In order to get access to this endpoint, contact our support team.

        Args:
          attempt_code: The fixed attempt code that will validate verification attempts for this phone
              number.

          phone_number: An E.164 formatted phone number to add to the sandbox list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v2/verification/management/phone-numbers/sandbox",
            body=await async_maybe_transform(
                {
                    "attempt_code": attempt_code,
                    "phone_number": phone_number,
                },
                sandbox_add_phone_number_params.SandboxAddPhoneNumberParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxAddPhoneNumberResponse,
        )

    async def delete_phone_number(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxDeletePhoneNumberResponse:
        """
        Remove a phone number from the sandbox list.

        This operation is idempotent - deleting a phone number that is not in the
        sandbox list will succeed without making any changes.

        In order to get access to this endpoint, contact our support team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._delete(
            path_template(
                "/v2/verification/management/phone-numbers/sandbox/{phone_number}", phone_number=phone_number
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxDeletePhoneNumberResponse,
        )

    async def list_phone_numbers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxListPhoneNumbersResponse:
        """Retrieve the list of sandbox phone numbers for the account.

        Sandbox numbers are
        test numbers that bypass the real verification flow and return a fixed attempt
        code.

        In order to get access to this endpoint, contact our support team.
        """
        return await self._get(
            "/v2/verification/management/phone-numbers/sandbox",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxListPhoneNumbersResponse,
        )


class SandboxResourceWithRawResponse:
    def __init__(self, sandbox: SandboxResource) -> None:
        self._sandbox = sandbox

        self.add_phone_number = to_raw_response_wrapper(
            sandbox.add_phone_number,
        )
        self.delete_phone_number = to_raw_response_wrapper(
            sandbox.delete_phone_number,
        )
        self.list_phone_numbers = to_raw_response_wrapper(
            sandbox.list_phone_numbers,
        )


class AsyncSandboxResourceWithRawResponse:
    def __init__(self, sandbox: AsyncSandboxResource) -> None:
        self._sandbox = sandbox

        self.add_phone_number = async_to_raw_response_wrapper(
            sandbox.add_phone_number,
        )
        self.delete_phone_number = async_to_raw_response_wrapper(
            sandbox.delete_phone_number,
        )
        self.list_phone_numbers = async_to_raw_response_wrapper(
            sandbox.list_phone_numbers,
        )


class SandboxResourceWithStreamingResponse:
    def __init__(self, sandbox: SandboxResource) -> None:
        self._sandbox = sandbox

        self.add_phone_number = to_streamed_response_wrapper(
            sandbox.add_phone_number,
        )
        self.delete_phone_number = to_streamed_response_wrapper(
            sandbox.delete_phone_number,
        )
        self.list_phone_numbers = to_streamed_response_wrapper(
            sandbox.list_phone_numbers,
        )


class AsyncSandboxResourceWithStreamingResponse:
    def __init__(self, sandbox: AsyncSandboxResource) -> None:
        self._sandbox = sandbox

        self.add_phone_number = async_to_streamed_response_wrapper(
            sandbox.add_phone_number,
        )
        self.delete_phone_number = async_to_streamed_response_wrapper(
            sandbox.delete_phone_number,
        )
        self.list_phone_numbers = async_to_streamed_response_wrapper(
            sandbox.list_phone_numbers,
        )
