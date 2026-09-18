# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.verification.phone import history_list_params
from ....types.verification.phone.history_list_response import HistoryListResponse
from ....types.verification.phone.history_retrieve_response import HistoryRetrieveResponse

__all__ = ["HistoryResource", "AsyncHistoryResource"]


class HistoryResource(SyncAPIResource):
    """Verify phone numbers."""

    @cached_property
    def with_raw_response(self) -> HistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return HistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return HistoryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HistoryRetrieveResponse:
        """
        Retrieve everything Prelude recorded for one phone verification: its outcome and
        the device, network and anti-fraud context it was created in, the chronological
        timeline of every message attempt and code check, and the anti-fraud signals you
        forwarded.

        The identifier is the `id` returned by
        [Create or retry a verification](/verify/v2/api-reference/create-or-retry-a-verification)
        or the `verification_id` of the verification webhooks. Both `lifecycle` and
        `signals` are optional: a verification can resolve with its top-level fields
        alone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v2/verification/phone/history/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HistoryRetrieveResponse,
        )

    def list(
        self,
        *,
        channels: List[Literal["sms", "rcs", "whatsapp", "viber", "zalo", "telegram", "voice", "silent"]] | Omit = omit,
        cursor: str | Omit = omit,
        device_platform: Literal["android", "ios", "ipados", "tvos", "web"] | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        max_attempts: int | Omit = omit,
        min_attempts: int | Omit = omit,
        phone_number: str | Omit = omit,
        region: str | Omit = omit,
        status: Literal[
            "converted",
            "not_converted",
            "pending_check",
            "sent",
            "challenged",
            "suspected_fraud",
            "in_blocklist",
            "invalid_line",
            "invalid_number",
            "rate_limited",
            "expired_signals",
            "shadowed",
        ]
        | Omit = omit,
        template_id: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HistoryListResponse:
        """
        List your phone verifications, most recent first, one entry per verification
        with its outcome, channels, attempts and cost. Every filter is optional and they
        combine with AND.

        Use it to find every verification a phone number went through from your support
        tooling, then
        [Get a phone verification](/verify/v2/api-reference/history/get-a-phone-verification)
        for the full timeline of one of them. A cursor is bound to the filters that
        produced it: pass `next_cursor` back with the exact same query parameters.

        Args:
          channels: Only verifications that could use one of these channels. Repeat the parameter
              for several values.

          cursor: Pagination cursor from the previous response.

          device_platform: Only verifications created from this device platform.

          from_: Only verifications created at or after this RFC 3339 timestamp. Goes with `to`,
              at most 6 months apart. Without them the whole history is searched.

          limit: Maximum number of verifications to return per page.

          max_attempts: Only verifications that sent at most this many messages. `0` keeps the
              verifications that never sent one.

          min_attempts: Only verifications that sent at least this many messages.

          phone_number: Only verifications targeting this E.164 phone number. The leading `+` may be
              omitted.

          region: Only verifications of phone numbers from this region, as an ISO 3166-1 alpha-2
              code.

          status: Only verifications in this status. `pending_check` cannot be filtered on.

          template_id: Only verifications sent with this template, as returned in `template_id` by
              [Get a phone verification](/verify/v2/api-reference/history/get-a-phone-verification).
              Built-in templates (`prelude:*`) cannot be filtered on.

          to: Only verifications created at or before this RFC 3339 timestamp. Goes with
              `from`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/verification/phone/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "channels": channels,
                        "cursor": cursor,
                        "device_platform": device_platform,
                        "from_": from_,
                        "limit": limit,
                        "max_attempts": max_attempts,
                        "min_attempts": min_attempts,
                        "phone_number": phone_number,
                        "region": region,
                        "status": status,
                        "template_id": template_id,
                        "to": to,
                    },
                    history_list_params.HistoryListParams,
                ),
            ),
            cast_to=HistoryListResponse,
        )


class AsyncHistoryResource(AsyncAPIResource):
    """Verify phone numbers."""

    @cached_property
    def with_raw_response(self) -> AsyncHistoryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncHistoryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHistoryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return AsyncHistoryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HistoryRetrieveResponse:
        """
        Retrieve everything Prelude recorded for one phone verification: its outcome and
        the device, network and anti-fraud context it was created in, the chronological
        timeline of every message attempt and code check, and the anti-fraud signals you
        forwarded.

        The identifier is the `id` returned by
        [Create or retry a verification](/verify/v2/api-reference/create-or-retry-a-verification)
        or the `verification_id` of the verification webhooks. Both `lifecycle` and
        `signals` are optional: a verification can resolve with its top-level fields
        alone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v2/verification/phone/history/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=HistoryRetrieveResponse,
        )

    async def list(
        self,
        *,
        channels: List[Literal["sms", "rcs", "whatsapp", "viber", "zalo", "telegram", "voice", "silent"]] | Omit = omit,
        cursor: str | Omit = omit,
        device_platform: Literal["android", "ios", "ipados", "tvos", "web"] | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        max_attempts: int | Omit = omit,
        min_attempts: int | Omit = omit,
        phone_number: str | Omit = omit,
        region: str | Omit = omit,
        status: Literal[
            "converted",
            "not_converted",
            "pending_check",
            "sent",
            "challenged",
            "suspected_fraud",
            "in_blocklist",
            "invalid_line",
            "invalid_number",
            "rate_limited",
            "expired_signals",
            "shadowed",
        ]
        | Omit = omit,
        template_id: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> HistoryListResponse:
        """
        List your phone verifications, most recent first, one entry per verification
        with its outcome, channels, attempts and cost. Every filter is optional and they
        combine with AND.

        Use it to find every verification a phone number went through from your support
        tooling, then
        [Get a phone verification](/verify/v2/api-reference/history/get-a-phone-verification)
        for the full timeline of one of them. A cursor is bound to the filters that
        produced it: pass `next_cursor` back with the exact same query parameters.

        Args:
          channels: Only verifications that could use one of these channels. Repeat the parameter
              for several values.

          cursor: Pagination cursor from the previous response.

          device_platform: Only verifications created from this device platform.

          from_: Only verifications created at or after this RFC 3339 timestamp. Goes with `to`,
              at most 6 months apart. Without them the whole history is searched.

          limit: Maximum number of verifications to return per page.

          max_attempts: Only verifications that sent at most this many messages. `0` keeps the
              verifications that never sent one.

          min_attempts: Only verifications that sent at least this many messages.

          phone_number: Only verifications targeting this E.164 phone number. The leading `+` may be
              omitted.

          region: Only verifications of phone numbers from this region, as an ISO 3166-1 alpha-2
              code.

          status: Only verifications in this status. `pending_check` cannot be filtered on.

          template_id: Only verifications sent with this template, as returned in `template_id` by
              [Get a phone verification](/verify/v2/api-reference/history/get-a-phone-verification).
              Built-in templates (`prelude:*`) cannot be filtered on.

          to: Only verifications created at or before this RFC 3339 timestamp. Goes with
              `from`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/verification/phone/history",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "channels": channels,
                        "cursor": cursor,
                        "device_platform": device_platform,
                        "from_": from_,
                        "limit": limit,
                        "max_attempts": max_attempts,
                        "min_attempts": min_attempts,
                        "phone_number": phone_number,
                        "region": region,
                        "status": status,
                        "template_id": template_id,
                        "to": to,
                    },
                    history_list_params.HistoryListParams,
                ),
            ),
            cast_to=HistoryListResponse,
        )


class HistoryResourceWithRawResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

        self.retrieve = to_raw_response_wrapper(
            history.retrieve,
        )
        self.list = to_raw_response_wrapper(
            history.list,
        )


class AsyncHistoryResourceWithRawResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.retrieve = async_to_raw_response_wrapper(
            history.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            history.list,
        )


class HistoryResourceWithStreamingResponse:
    def __init__(self, history: HistoryResource) -> None:
        self._history = history

        self.retrieve = to_streamed_response_wrapper(
            history.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            history.list,
        )


class AsyncHistoryResourceWithStreamingResponse:
    def __init__(self, history: AsyncHistoryResource) -> None:
        self._history = history

        self.retrieve = async_to_streamed_response_wrapper(
            history.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            history.list,
        )
