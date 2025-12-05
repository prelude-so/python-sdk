# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    notify_send_params,
    notify_send_batch_params,
    notify_list_subscription_configs_params,
    notify_list_subscription_phone_numbers_params,
    notify_list_subscription_phone_number_events_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.notify_send_response import NotifySendResponse
from ..types.notify_send_batch_response import NotifySendBatchResponse
from ..types.notify_get_subscription_config_response import NotifyGetSubscriptionConfigResponse
from ..types.notify_list_subscription_configs_response import NotifyListSubscriptionConfigsResponse
from ..types.notify_get_subscription_phone_number_response import NotifyGetSubscriptionPhoneNumberResponse
from ..types.notify_list_subscription_phone_numbers_response import NotifyListSubscriptionPhoneNumbersResponse
from ..types.notify_list_subscription_phone_number_events_response import (
    NotifyListSubscriptionPhoneNumberEventsResponse,
)

__all__ = ["NotifyResource", "AsyncNotifyResource"]


class NotifyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return NotifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return NotifyResourceWithStreamingResponse(self)

    def get_subscription_config(
        self,
        config_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotifyGetSubscriptionConfigResponse:
        """
        Retrieve a specific subscription management configuration by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return self._get(
            f"/v2/notify/management/subscriptions/{config_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotifyGetSubscriptionConfigResponse,
        )

    def get_subscription_phone_number(
        self,
        phone_number: str,
        *,
        config_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotifyGetSubscriptionPhoneNumberResponse:
        """
        Retrieve the current subscription status for a specific phone number within a
        subscription configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            f"/v2/notify/management/subscriptions/{config_id}/phone_numbers/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotifyGetSubscriptionPhoneNumberResponse,
        )

    def list_subscription_configs(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotifyListSubscriptionConfigsResponse:
        """
        Retrieve a paginated list of subscription management configurations for your
        account.

        Each configuration represents a subscription management setup with phone numbers
        for receiving opt-out/opt-in requests and a callback URL for webhook events.

        Args:
          cursor: Pagination cursor from the previous response

          limit: Maximum number of configurations to return per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v2/notify/management/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    notify_list_subscription_configs_params.NotifyListSubscriptionConfigsParams,
                ),
            ),
            cast_to=NotifyListSubscriptionConfigsResponse,
        )

    def list_subscription_phone_number_events(
        self,
        phone_number: str,
        *,
        config_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotifyListSubscriptionPhoneNumberEventsResponse:
        """
        Retrieve a paginated list of subscription events (status changes) for a specific
        phone number within a subscription configuration.

        Events are ordered by timestamp in descending order (most recent first).

        Args:
          cursor: Pagination cursor from the previous response

          limit: Maximum number of events to return per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            f"/v2/notify/management/subscriptions/{config_id}/phone_numbers/{phone_number}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    notify_list_subscription_phone_number_events_params.NotifyListSubscriptionPhoneNumberEventsParams,
                ),
            ),
            cast_to=NotifyListSubscriptionPhoneNumberEventsResponse,
        )

    def list_subscription_phone_numbers(
        self,
        config_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        state: Literal["SUB", "UNSUB"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotifyListSubscriptionPhoneNumbersResponse:
        """
        Retrieve a paginated list of phone numbers and their subscription statuses for a
        specific subscription configuration.

        You can optionally filter by subscription state (SUB or UNSUB).

        Args:
          cursor: Pagination cursor from the previous response

          limit: Maximum number of phone numbers to return per page

          state: Filter by subscription state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return self._get(
            f"/v2/notify/management/subscriptions/{config_id}/phone_numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "state": state,
                    },
                    notify_list_subscription_phone_numbers_params.NotifyListSubscriptionPhoneNumbersParams,
                ),
            ),
            cast_to=NotifyListSubscriptionPhoneNumbersResponse,
        )

    def send(
        self,
        *,
        template_id: str,
        to: str,
        callback_url: str | Omit = omit,
        correlation_id: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        from_: str | Omit = omit,
        locale: str | Omit = omit,
        preferred_channel: Literal["sms", "whatsapp"] | Omit = omit,
        schedule_at: Union[str, datetime] | Omit = omit,
        variables: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotifySendResponse:
        """
        Send transactional and marketing messages to your users via SMS and WhatsApp
        with automatic compliance enforcement.

        Args:
          template_id: The template identifier configured by your Customer Success team.

          to: The recipient's phone number in E.164 format.

          callback_url: The URL where webhooks will be sent for message delivery events.

          correlation_id: A user-defined identifier to correlate this message with your internal systems.
              It is returned in the response and any webhook events that refer to this
              message.

          expires_at: The message expiration date in RFC3339 format. The message will not be sent if
              this time is reached.

          from_: The Sender ID. Must be approved for your account.

          locale: A BCP-47 formatted locale string with the language the text message will be sent
              to. If there's no locale set, the language will be determined by the country
              code of the phone number. If the language specified doesn't exist, the default
              set on the template will be used.

          preferred_channel: The preferred channel to be used in priority for message delivery. If the
              channel is unavailable, the system will fallback to other available channels.

          schedule_at: Schedule the message for future delivery in RFC3339 format. Marketing messages
              can be scheduled up to 90 days in advance and will be automatically adjusted for
              compliance with local time window restrictions.

          variables: The variables to be replaced in the template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/notify",
            body=maybe_transform(
                {
                    "template_id": template_id,
                    "to": to,
                    "callback_url": callback_url,
                    "correlation_id": correlation_id,
                    "expires_at": expires_at,
                    "from_": from_,
                    "locale": locale,
                    "preferred_channel": preferred_channel,
                    "schedule_at": schedule_at,
                    "variables": variables,
                },
                notify_send_params.NotifySendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotifySendResponse,
        )

    def send_batch(
        self,
        *,
        template_id: str,
        to: SequenceNotStr[str],
        callback_url: str | Omit = omit,
        correlation_id: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        from_: str | Omit = omit,
        locale: str | Omit = omit,
        preferred_channel: Literal["sms", "whatsapp"] | Omit = omit,
        schedule_at: Union[str, datetime] | Omit = omit,
        variables: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotifySendBatchResponse:
        """
        Send the same message to multiple recipients in a single request.

        Args:
          template_id: The template identifier configured by your Customer Success team.

          to: The list of recipients' phone numbers in E.164 format.

          callback_url: The URL where webhooks will be sent for delivery events.

          correlation_id: A user-defined identifier to correlate this request with your internal systems.

          expires_at: The message expiration date in RFC3339 format. Messages will not be sent after
              this time.

          from_: The Sender ID. Must be approved for your account.

          locale: A BCP-47 formatted locale string.

          preferred_channel: Preferred channel for delivery. If unavailable, automatic fallback applies.

          schedule_at: Schedule delivery in RFC3339 format. Marketing sends may be adjusted to comply
              with local time windows.

          variables: The variables to be replaced in the template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v2/notify/batch",
            body=maybe_transform(
                {
                    "template_id": template_id,
                    "to": to,
                    "callback_url": callback_url,
                    "correlation_id": correlation_id,
                    "expires_at": expires_at,
                    "from_": from_,
                    "locale": locale,
                    "preferred_channel": preferred_channel,
                    "schedule_at": schedule_at,
                    "variables": variables,
                },
                notify_send_batch_params.NotifySendBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotifySendBatchResponse,
        )


class AsyncNotifyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncNotifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return AsyncNotifyResourceWithStreamingResponse(self)

    async def get_subscription_config(
        self,
        config_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotifyGetSubscriptionConfigResponse:
        """
        Retrieve a specific subscription management configuration by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return await self._get(
            f"/v2/notify/management/subscriptions/{config_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotifyGetSubscriptionConfigResponse,
        )

    async def get_subscription_phone_number(
        self,
        phone_number: str,
        *,
        config_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotifyGetSubscriptionPhoneNumberResponse:
        """
        Retrieve the current subscription status for a specific phone number within a
        subscription configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            f"/v2/notify/management/subscriptions/{config_id}/phone_numbers/{phone_number}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotifyGetSubscriptionPhoneNumberResponse,
        )

    async def list_subscription_configs(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotifyListSubscriptionConfigsResponse:
        """
        Retrieve a paginated list of subscription management configurations for your
        account.

        Each configuration represents a subscription management setup with phone numbers
        for receiving opt-out/opt-in requests and a callback URL for webhook events.

        Args:
          cursor: Pagination cursor from the previous response

          limit: Maximum number of configurations to return per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v2/notify/management/subscriptions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    notify_list_subscription_configs_params.NotifyListSubscriptionConfigsParams,
                ),
            ),
            cast_to=NotifyListSubscriptionConfigsResponse,
        )

    async def list_subscription_phone_number_events(
        self,
        phone_number: str,
        *,
        config_id: str,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotifyListSubscriptionPhoneNumberEventsResponse:
        """
        Retrieve a paginated list of subscription events (status changes) for a specific
        phone number within a subscription configuration.

        Events are ordered by timestamp in descending order (most recent first).

        Args:
          cursor: Pagination cursor from the previous response

          limit: Maximum number of events to return per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            f"/v2/notify/management/subscriptions/{config_id}/phone_numbers/{phone_number}/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    notify_list_subscription_phone_number_events_params.NotifyListSubscriptionPhoneNumberEventsParams,
                ),
            ),
            cast_to=NotifyListSubscriptionPhoneNumberEventsResponse,
        )

    async def list_subscription_phone_numbers(
        self,
        config_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        state: Literal["SUB", "UNSUB"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotifyListSubscriptionPhoneNumbersResponse:
        """
        Retrieve a paginated list of phone numbers and their subscription statuses for a
        specific subscription configuration.

        You can optionally filter by subscription state (SUB or UNSUB).

        Args:
          cursor: Pagination cursor from the previous response

          limit: Maximum number of phone numbers to return per page

          state: Filter by subscription state

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return await self._get(
            f"/v2/notify/management/subscriptions/{config_id}/phone_numbers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "state": state,
                    },
                    notify_list_subscription_phone_numbers_params.NotifyListSubscriptionPhoneNumbersParams,
                ),
            ),
            cast_to=NotifyListSubscriptionPhoneNumbersResponse,
        )

    async def send(
        self,
        *,
        template_id: str,
        to: str,
        callback_url: str | Omit = omit,
        correlation_id: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        from_: str | Omit = omit,
        locale: str | Omit = omit,
        preferred_channel: Literal["sms", "whatsapp"] | Omit = omit,
        schedule_at: Union[str, datetime] | Omit = omit,
        variables: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotifySendResponse:
        """
        Send transactional and marketing messages to your users via SMS and WhatsApp
        with automatic compliance enforcement.

        Args:
          template_id: The template identifier configured by your Customer Success team.

          to: The recipient's phone number in E.164 format.

          callback_url: The URL where webhooks will be sent for message delivery events.

          correlation_id: A user-defined identifier to correlate this message with your internal systems.
              It is returned in the response and any webhook events that refer to this
              message.

          expires_at: The message expiration date in RFC3339 format. The message will not be sent if
              this time is reached.

          from_: The Sender ID. Must be approved for your account.

          locale: A BCP-47 formatted locale string with the language the text message will be sent
              to. If there's no locale set, the language will be determined by the country
              code of the phone number. If the language specified doesn't exist, the default
              set on the template will be used.

          preferred_channel: The preferred channel to be used in priority for message delivery. If the
              channel is unavailable, the system will fallback to other available channels.

          schedule_at: Schedule the message for future delivery in RFC3339 format. Marketing messages
              can be scheduled up to 90 days in advance and will be automatically adjusted for
              compliance with local time window restrictions.

          variables: The variables to be replaced in the template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/notify",
            body=await async_maybe_transform(
                {
                    "template_id": template_id,
                    "to": to,
                    "callback_url": callback_url,
                    "correlation_id": correlation_id,
                    "expires_at": expires_at,
                    "from_": from_,
                    "locale": locale,
                    "preferred_channel": preferred_channel,
                    "schedule_at": schedule_at,
                    "variables": variables,
                },
                notify_send_params.NotifySendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotifySendResponse,
        )

    async def send_batch(
        self,
        *,
        template_id: str,
        to: SequenceNotStr[str],
        callback_url: str | Omit = omit,
        correlation_id: str | Omit = omit,
        expires_at: Union[str, datetime] | Omit = omit,
        from_: str | Omit = omit,
        locale: str | Omit = omit,
        preferred_channel: Literal["sms", "whatsapp"] | Omit = omit,
        schedule_at: Union[str, datetime] | Omit = omit,
        variables: Dict[str, str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotifySendBatchResponse:
        """
        Send the same message to multiple recipients in a single request.

        Args:
          template_id: The template identifier configured by your Customer Success team.

          to: The list of recipients' phone numbers in E.164 format.

          callback_url: The URL where webhooks will be sent for delivery events.

          correlation_id: A user-defined identifier to correlate this request with your internal systems.

          expires_at: The message expiration date in RFC3339 format. Messages will not be sent after
              this time.

          from_: The Sender ID. Must be approved for your account.

          locale: A BCP-47 formatted locale string.

          preferred_channel: Preferred channel for delivery. If unavailable, automatic fallback applies.

          schedule_at: Schedule delivery in RFC3339 format. Marketing sends may be adjusted to comply
              with local time windows.

          variables: The variables to be replaced in the template.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v2/notify/batch",
            body=await async_maybe_transform(
                {
                    "template_id": template_id,
                    "to": to,
                    "callback_url": callback_url,
                    "correlation_id": correlation_id,
                    "expires_at": expires_at,
                    "from_": from_,
                    "locale": locale,
                    "preferred_channel": preferred_channel,
                    "schedule_at": schedule_at,
                    "variables": variables,
                },
                notify_send_batch_params.NotifySendBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotifySendBatchResponse,
        )


class NotifyResourceWithRawResponse:
    def __init__(self, notify: NotifyResource) -> None:
        self._notify = notify

        self.get_subscription_config = to_raw_response_wrapper(
            notify.get_subscription_config,
        )
        self.get_subscription_phone_number = to_raw_response_wrapper(
            notify.get_subscription_phone_number,
        )
        self.list_subscription_configs = to_raw_response_wrapper(
            notify.list_subscription_configs,
        )
        self.list_subscription_phone_number_events = to_raw_response_wrapper(
            notify.list_subscription_phone_number_events,
        )
        self.list_subscription_phone_numbers = to_raw_response_wrapper(
            notify.list_subscription_phone_numbers,
        )
        self.send = to_raw_response_wrapper(
            notify.send,
        )
        self.send_batch = to_raw_response_wrapper(
            notify.send_batch,
        )


class AsyncNotifyResourceWithRawResponse:
    def __init__(self, notify: AsyncNotifyResource) -> None:
        self._notify = notify

        self.get_subscription_config = async_to_raw_response_wrapper(
            notify.get_subscription_config,
        )
        self.get_subscription_phone_number = async_to_raw_response_wrapper(
            notify.get_subscription_phone_number,
        )
        self.list_subscription_configs = async_to_raw_response_wrapper(
            notify.list_subscription_configs,
        )
        self.list_subscription_phone_number_events = async_to_raw_response_wrapper(
            notify.list_subscription_phone_number_events,
        )
        self.list_subscription_phone_numbers = async_to_raw_response_wrapper(
            notify.list_subscription_phone_numbers,
        )
        self.send = async_to_raw_response_wrapper(
            notify.send,
        )
        self.send_batch = async_to_raw_response_wrapper(
            notify.send_batch,
        )


class NotifyResourceWithStreamingResponse:
    def __init__(self, notify: NotifyResource) -> None:
        self._notify = notify

        self.get_subscription_config = to_streamed_response_wrapper(
            notify.get_subscription_config,
        )
        self.get_subscription_phone_number = to_streamed_response_wrapper(
            notify.get_subscription_phone_number,
        )
        self.list_subscription_configs = to_streamed_response_wrapper(
            notify.list_subscription_configs,
        )
        self.list_subscription_phone_number_events = to_streamed_response_wrapper(
            notify.list_subscription_phone_number_events,
        )
        self.list_subscription_phone_numbers = to_streamed_response_wrapper(
            notify.list_subscription_phone_numbers,
        )
        self.send = to_streamed_response_wrapper(
            notify.send,
        )
        self.send_batch = to_streamed_response_wrapper(
            notify.send_batch,
        )


class AsyncNotifyResourceWithStreamingResponse:
    def __init__(self, notify: AsyncNotifyResource) -> None:
        self._notify = notify

        self.get_subscription_config = async_to_streamed_response_wrapper(
            notify.get_subscription_config,
        )
        self.get_subscription_phone_number = async_to_streamed_response_wrapper(
            notify.get_subscription_phone_number,
        )
        self.list_subscription_configs = async_to_streamed_response_wrapper(
            notify.list_subscription_configs,
        )
        self.list_subscription_phone_number_events = async_to_streamed_response_wrapper(
            notify.list_subscription_phone_number_events,
        )
        self.list_subscription_phone_numbers = async_to_streamed_response_wrapper(
            notify.list_subscription_phone_numbers,
        )
        self.send = async_to_streamed_response_wrapper(
            notify.send,
        )
        self.send_batch = async_to_streamed_response_wrapper(
            notify.send_batch,
        )
