# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    verification_management_set_phone_number_params,
    verification_management_submit_sender_id_params,
    verification_management_delete_phone_number_params,
)
from .._types import Body, Query, Headers, NotGiven, not_given
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
from ..types.verification_management_list_sender_ids_response import VerificationManagementListSenderIDsResponse
from ..types.verification_management_set_phone_number_response import VerificationManagementSetPhoneNumberResponse
from ..types.verification_management_submit_sender_id_response import VerificationManagementSubmitSenderIDResponse
from ..types.verification_management_list_phone_numbers_response import VerificationManagementListPhoneNumbersResponse
from ..types.verification_management_delete_phone_number_response import VerificationManagementDeletePhoneNumberResponse

__all__ = ["VerificationManagementResource", "AsyncVerificationManagementResource"]


class VerificationManagementResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VerificationManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return VerificationManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerificationManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return VerificationManagementResourceWithStreamingResponse(self)

    def delete_phone_number(
        self,
        action: Literal["allow", "block"],
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationManagementDeletePhoneNumberResponse:
        """
        Remove a phone number from the allow or block list.

        This operation is idempotent - re-deleting the same phone number will not result
        in errors. If the phone number does not exist in the specified list, the
        operation will succeed without making any changes.

        In order to get access to this endpoint, contact our support team.

        Args:
          phone_number: An E.164 formatted phone number to remove from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return self._delete(
            f"/v2/verification/management/phone-numbers/{action}",
            body=maybe_transform(
                {"phone_number": phone_number},
                verification_management_delete_phone_number_params.VerificationManagementDeletePhoneNumberParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationManagementDeletePhoneNumberResponse,
        )

    def list_phone_numbers(
        self,
        action: Literal["allow", "block"],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationManagementListPhoneNumbersResponse:
        """
        Retrieve the list of phone numbers in the allow or block list.

        In order to get access to this endpoint, contact our support team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return self._get(
            f"/v2/verification/management/phone-numbers/{action}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationManagementListPhoneNumbersResponse,
        )

    def list_sender_ids(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationManagementListSenderIDsResponse:
        """
        Retrieve sender IDs list.

        In order to get access to this endpoint, contact our support team.
        """
        return self._get(
            "/v2/verification/management/sender-id",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationManagementListSenderIDsResponse,
        )

    def set_phone_number(
        self,
        action: Literal["allow", "block"],
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationManagementSetPhoneNumberResponse:
        """
        Add a phone number to the allow or block list.

        This operation is idempotent - re-adding the same phone number will not result
        in duplicate entries or errors. If the phone number already exists in the
        specified list, the operation will succeed without making any changes.

        In order to get access to this endpoint, contact our support team.

        Args:
          phone_number: An E.164 formatted phone number to add to the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return self._post(
            f"/v2/verification/management/phone-numbers/{action}",
            body=maybe_transform(
                {"phone_number": phone_number},
                verification_management_set_phone_number_params.VerificationManagementSetPhoneNumberParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationManagementSetPhoneNumberResponse,
        )

    def submit_sender_id(
        self,
        *,
        sender_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationManagementSubmitSenderIDResponse:
        """
        This endpoint allows you to submit a new sender ID for verification purposes.

        In order to get access to this endpoint, contact our support team.

        Args:
          sender_id: The sender ID to add.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/verification/management/sender-id",
            body=maybe_transform(
                {"sender_id": sender_id},
                verification_management_submit_sender_id_params.VerificationManagementSubmitSenderIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationManagementSubmitSenderIDResponse,
        )


class AsyncVerificationManagementResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVerificationManagementResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncVerificationManagementResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerificationManagementResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return AsyncVerificationManagementResourceWithStreamingResponse(self)

    async def delete_phone_number(
        self,
        action: Literal["allow", "block"],
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationManagementDeletePhoneNumberResponse:
        """
        Remove a phone number from the allow or block list.

        This operation is idempotent - re-deleting the same phone number will not result
        in errors. If the phone number does not exist in the specified list, the
        operation will succeed without making any changes.

        In order to get access to this endpoint, contact our support team.

        Args:
          phone_number: An E.164 formatted phone number to remove from the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return await self._delete(
            f"/v2/verification/management/phone-numbers/{action}",
            body=await async_maybe_transform(
                {"phone_number": phone_number},
                verification_management_delete_phone_number_params.VerificationManagementDeletePhoneNumberParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationManagementDeletePhoneNumberResponse,
        )

    async def list_phone_numbers(
        self,
        action: Literal["allow", "block"],
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationManagementListPhoneNumbersResponse:
        """
        Retrieve the list of phone numbers in the allow or block list.

        In order to get access to this endpoint, contact our support team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return await self._get(
            f"/v2/verification/management/phone-numbers/{action}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationManagementListPhoneNumbersResponse,
        )

    async def list_sender_ids(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationManagementListSenderIDsResponse:
        """
        Retrieve sender IDs list.

        In order to get access to this endpoint, contact our support team.
        """
        return await self._get(
            "/v2/verification/management/sender-id",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationManagementListSenderIDsResponse,
        )

    async def set_phone_number(
        self,
        action: Literal["allow", "block"],
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationManagementSetPhoneNumberResponse:
        """
        Add a phone number to the allow or block list.

        This operation is idempotent - re-adding the same phone number will not result
        in duplicate entries or errors. If the phone number already exists in the
        specified list, the operation will succeed without making any changes.

        In order to get access to this endpoint, contact our support team.

        Args:
          phone_number: An E.164 formatted phone number to add to the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not action:
            raise ValueError(f"Expected a non-empty value for `action` but received {action!r}")
        return await self._post(
            f"/v2/verification/management/phone-numbers/{action}",
            body=await async_maybe_transform(
                {"phone_number": phone_number},
                verification_management_set_phone_number_params.VerificationManagementSetPhoneNumberParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationManagementSetPhoneNumberResponse,
        )

    async def submit_sender_id(
        self,
        *,
        sender_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerificationManagementSubmitSenderIDResponse:
        """
        This endpoint allows you to submit a new sender ID for verification purposes.

        In order to get access to this endpoint, contact our support team.

        Args:
          sender_id: The sender ID to add.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/verification/management/sender-id",
            body=await async_maybe_transform(
                {"sender_id": sender_id},
                verification_management_submit_sender_id_params.VerificationManagementSubmitSenderIDParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VerificationManagementSubmitSenderIDResponse,
        )


class VerificationManagementResourceWithRawResponse:
    def __init__(self, verification_management: VerificationManagementResource) -> None:
        self._verification_management = verification_management

        self.delete_phone_number = to_raw_response_wrapper(
            verification_management.delete_phone_number,
        )
        self.list_phone_numbers = to_raw_response_wrapper(
            verification_management.list_phone_numbers,
        )
        self.list_sender_ids = to_raw_response_wrapper(
            verification_management.list_sender_ids,
        )
        self.set_phone_number = to_raw_response_wrapper(
            verification_management.set_phone_number,
        )
        self.submit_sender_id = to_raw_response_wrapper(
            verification_management.submit_sender_id,
        )


class AsyncVerificationManagementResourceWithRawResponse:
    def __init__(self, verification_management: AsyncVerificationManagementResource) -> None:
        self._verification_management = verification_management

        self.delete_phone_number = async_to_raw_response_wrapper(
            verification_management.delete_phone_number,
        )
        self.list_phone_numbers = async_to_raw_response_wrapper(
            verification_management.list_phone_numbers,
        )
        self.list_sender_ids = async_to_raw_response_wrapper(
            verification_management.list_sender_ids,
        )
        self.set_phone_number = async_to_raw_response_wrapper(
            verification_management.set_phone_number,
        )
        self.submit_sender_id = async_to_raw_response_wrapper(
            verification_management.submit_sender_id,
        )


class VerificationManagementResourceWithStreamingResponse:
    def __init__(self, verification_management: VerificationManagementResource) -> None:
        self._verification_management = verification_management

        self.delete_phone_number = to_streamed_response_wrapper(
            verification_management.delete_phone_number,
        )
        self.list_phone_numbers = to_streamed_response_wrapper(
            verification_management.list_phone_numbers,
        )
        self.list_sender_ids = to_streamed_response_wrapper(
            verification_management.list_sender_ids,
        )
        self.set_phone_number = to_streamed_response_wrapper(
            verification_management.set_phone_number,
        )
        self.submit_sender_id = to_streamed_response_wrapper(
            verification_management.submit_sender_id,
        )


class AsyncVerificationManagementResourceWithStreamingResponse:
    def __init__(self, verification_management: AsyncVerificationManagementResource) -> None:
        self._verification_management = verification_management

        self.delete_phone_number = async_to_streamed_response_wrapper(
            verification_management.delete_phone_number,
        )
        self.list_phone_numbers = async_to_streamed_response_wrapper(
            verification_management.list_phone_numbers,
        )
        self.list_sender_ids = async_to_streamed_response_wrapper(
            verification_management.list_sender_ids,
        )
        self.set_phone_number = async_to_streamed_response_wrapper(
            verification_management.set_phone_number,
        )
        self.submit_sender_id = async_to_streamed_response_wrapper(
            verification_management.submit_sender_id,
        )
