# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import authentication_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .feedback import (
    FeedbackResource,
    AsyncFeedbackResource,
    FeedbackResourceWithRawResponse,
    AsyncFeedbackResourceWithRawResponse,
    FeedbackResourceWithStreamingResponse,
    AsyncFeedbackResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.authentication_create_response import AuthenticationCreateResponse
from ...types.authentication_retrieve_response import AuthenticationRetrieveResponse

__all__ = ["AuthenticationResource", "AsyncAuthenticationResource"]


class AuthenticationResource(SyncAPIResource):
    @cached_property
    def feedback(self) -> FeedbackResource:
        return FeedbackResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthenticationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prelude-python#accessing-raw-response-data-eg-headers
        """
        return AuthenticationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthenticationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prelude-python#with_streaming_response
        """
        return AuthenticationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_uuid: str,
        phone_number: str,
        app_realm: str | NotGiven = NOT_GIVEN,
        app_version: str | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        correlation_id: str | NotGiven = NOT_GIVEN,
        device_id: str | NotGiven = NOT_GIVEN,
        device_model: str | NotGiven = NOT_GIVEN,
        device_type: Literal["IOS", "ANDROID", "WEB"] | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        is_returning_user: bool | NotGiven = NOT_GIVEN,
        locale: str | NotGiven = NOT_GIVEN,
        os_version: str | NotGiven = NOT_GIVEN,
        sender_id: str | NotGiven = NOT_GIVEN,
        template_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationCreateResponse:
        """
        Send a code

        Args:
          customer_uuid: Your customer UUID, which can be found in the API settings in the dashboard.

          phone_number: An E.164 formatted phone number to send the OTP to.

          app_realm: The Android SMS Retriever API hash code that identifies your app. This allows
              you to automatically retrieve and fill the OTP code on Android devices.

          app_version: The version of your application.

          callback_url: A webhook URL to which delivery statuses will be sent.

          correlation_id: A unique, user-defined identifier that will be included in webhook events

          device_id: Unique identifier for the user's device. For Android, this corresponds to the
              `ANDROID_ID` and for iOS, this corresponds to the `identifierForVendor`.

          device_model: The model of the user's device.

          device_type: The type of device the user is using.

          ip: The IP address of the user's device.

          is_returning_user: This signal should do more than just confirm if a user is returning to your app;
              it should provide a higher level of trust, indicating that the user is genuine.
              For more details, refer to [Signals](/guides/prevent-fraud#signals).

          locale: A BCP-47 locale indicating the language the SMS should be sent to; if this is
              not set, the SMS will be sent to the language specified by the country code of
              the message. If we don't support the language set, the message will be sent in
              US English (en-US).

          os_version: The version of the user's device operating system.

          sender_id: The Sender ID to use when sending the message.

          template_id: The template id associated with the message content variant to be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/authentication",
            body=maybe_transform(
                {
                    "customer_uuid": customer_uuid,
                    "phone_number": phone_number,
                    "app_realm": app_realm,
                    "app_version": app_version,
                    "callback_url": callback_url,
                    "correlation_id": correlation_id,
                    "device_id": device_id,
                    "device_model": device_model,
                    "device_type": device_type,
                    "ip": ip,
                    "is_returning_user": is_returning_user,
                    "locale": locale,
                    "os_version": os_version,
                    "sender_id": sender_id,
                    "template_id": template_id,
                },
                authentication_create_params.AuthenticationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationCreateResponse,
        )

    def retrieve(
        self,
        auth_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationRetrieveResponse:
        """
        Get authentication status

        Args:
          auth_uuid: The UUID of the authentication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_uuid:
            raise ValueError(f"Expected a non-empty value for `auth_uuid` but received {auth_uuid!r}")
        return self._get(
            f"/authentication/{auth_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationRetrieveResponse,
        )


class AsyncAuthenticationResource(AsyncAPIResource):
    @cached_property
    def feedback(self) -> AsyncFeedbackResource:
        return AsyncFeedbackResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthenticationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/prelude-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthenticationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthenticationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/prelude-python#with_streaming_response
        """
        return AsyncAuthenticationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_uuid: str,
        phone_number: str,
        app_realm: str | NotGiven = NOT_GIVEN,
        app_version: str | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        correlation_id: str | NotGiven = NOT_GIVEN,
        device_id: str | NotGiven = NOT_GIVEN,
        device_model: str | NotGiven = NOT_GIVEN,
        device_type: Literal["IOS", "ANDROID", "WEB"] | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        is_returning_user: bool | NotGiven = NOT_GIVEN,
        locale: str | NotGiven = NOT_GIVEN,
        os_version: str | NotGiven = NOT_GIVEN,
        sender_id: str | NotGiven = NOT_GIVEN,
        template_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationCreateResponse:
        """
        Send a code

        Args:
          customer_uuid: Your customer UUID, which can be found in the API settings in the dashboard.

          phone_number: An E.164 formatted phone number to send the OTP to.

          app_realm: The Android SMS Retriever API hash code that identifies your app. This allows
              you to automatically retrieve and fill the OTP code on Android devices.

          app_version: The version of your application.

          callback_url: A webhook URL to which delivery statuses will be sent.

          correlation_id: A unique, user-defined identifier that will be included in webhook events

          device_id: Unique identifier for the user's device. For Android, this corresponds to the
              `ANDROID_ID` and for iOS, this corresponds to the `identifierForVendor`.

          device_model: The model of the user's device.

          device_type: The type of device the user is using.

          ip: The IP address of the user's device.

          is_returning_user: This signal should do more than just confirm if a user is returning to your app;
              it should provide a higher level of trust, indicating that the user is genuine.
              For more details, refer to [Signals](/guides/prevent-fraud#signals).

          locale: A BCP-47 locale indicating the language the SMS should be sent to; if this is
              not set, the SMS will be sent to the language specified by the country code of
              the message. If we don't support the language set, the message will be sent in
              US English (en-US).

          os_version: The version of the user's device operating system.

          sender_id: The Sender ID to use when sending the message.

          template_id: The template id associated with the message content variant to be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/authentication",
            body=await async_maybe_transform(
                {
                    "customer_uuid": customer_uuid,
                    "phone_number": phone_number,
                    "app_realm": app_realm,
                    "app_version": app_version,
                    "callback_url": callback_url,
                    "correlation_id": correlation_id,
                    "device_id": device_id,
                    "device_model": device_model,
                    "device_type": device_type,
                    "ip": ip,
                    "is_returning_user": is_returning_user,
                    "locale": locale,
                    "os_version": os_version,
                    "sender_id": sender_id,
                    "template_id": template_id,
                },
                authentication_create_params.AuthenticationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationCreateResponse,
        )

    async def retrieve(
        self,
        auth_uuid: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationRetrieveResponse:
        """
        Get authentication status

        Args:
          auth_uuid: The UUID of the authentication.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not auth_uuid:
            raise ValueError(f"Expected a non-empty value for `auth_uuid` but received {auth_uuid!r}")
        return await self._get(
            f"/authentication/{auth_uuid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationRetrieveResponse,
        )


class AuthenticationResourceWithRawResponse:
    def __init__(self, authentication: AuthenticationResource) -> None:
        self._authentication = authentication

        self.create = to_raw_response_wrapper(
            authentication.create,
        )
        self.retrieve = to_raw_response_wrapper(
            authentication.retrieve,
        )

    @cached_property
    def feedback(self) -> FeedbackResourceWithRawResponse:
        return FeedbackResourceWithRawResponse(self._authentication.feedback)


class AsyncAuthenticationResourceWithRawResponse:
    def __init__(self, authentication: AsyncAuthenticationResource) -> None:
        self._authentication = authentication

        self.create = async_to_raw_response_wrapper(
            authentication.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            authentication.retrieve,
        )

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithRawResponse:
        return AsyncFeedbackResourceWithRawResponse(self._authentication.feedback)


class AuthenticationResourceWithStreamingResponse:
    def __init__(self, authentication: AuthenticationResource) -> None:
        self._authentication = authentication

        self.create = to_streamed_response_wrapper(
            authentication.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            authentication.retrieve,
        )

    @cached_property
    def feedback(self) -> FeedbackResourceWithStreamingResponse:
        return FeedbackResourceWithStreamingResponse(self._authentication.feedback)


class AsyncAuthenticationResourceWithStreamingResponse:
    def __init__(self, authentication: AsyncAuthenticationResource) -> None:
        self._authentication = authentication

        self.create = async_to_streamed_response_wrapper(
            authentication.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            authentication.retrieve,
        )

    @cached_property
    def feedback(self) -> AsyncFeedbackResourceWithStreamingResponse:
        return AsyncFeedbackResourceWithStreamingResponse(self._authentication.feedback)
