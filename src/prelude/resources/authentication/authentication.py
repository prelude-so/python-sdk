# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import AuthenticationCreateResponse, authentication_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .feedback import (
    Feedback,
    AsyncFeedback,
    FeedbackWithRawResponse,
    AsyncFeedbackWithRawResponse,
    FeedbackWithStreamingResponse,
    AsyncFeedbackWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["Authentication", "AsyncAuthentication"]


class Authentication(SyncAPIResource):
    @cached_property
    def feedback(self) -> Feedback:
        return Feedback(self._client)

    @cached_property
    def with_raw_response(self) -> AuthenticationWithRawResponse:
        return AuthenticationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthenticationWithStreamingResponse:
        return AuthenticationWithStreamingResponse(self)

    def create(
        self,
        *,
        customer_uuid: str,
        phone_number: str,
        app_realm: str | NotGiven = NOT_GIVEN,
        app_version: str | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        device_id: str | NotGiven = NOT_GIVEN,
        device_model: str | NotGiven = NOT_GIVEN,
        device_type: Literal["IOS", "ANDROID", "WEB"] | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        is_returning_user: bool | NotGiven = NOT_GIVEN,
        os_version: str | NotGiven = NOT_GIVEN,
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

          device_id: Unique identifier for the user's device. For Android, this corresponds to the
              `ANDROID_ID` and for iOS, this corresponds to the `identifierForVendor`.

          device_model: The model of the user's device.

          device_type: The type of device the user is using.

          ip: The IP address of the user's device.

          is_returning_user: Whether the user is a returning user on your app.

          os_version: The version of the user's device operating system.

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
                    "device_id": device_id,
                    "device_model": device_model,
                    "device_type": device_type,
                    "ip": ip,
                    "is_returning_user": is_returning_user,
                    "os_version": os_version,
                    "template_id": template_id,
                },
                authentication_create_params.AuthenticationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationCreateResponse,
        )


class AsyncAuthentication(AsyncAPIResource):
    @cached_property
    def feedback(self) -> AsyncFeedback:
        return AsyncFeedback(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthenticationWithRawResponse:
        return AsyncAuthenticationWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthenticationWithStreamingResponse:
        return AsyncAuthenticationWithStreamingResponse(self)

    async def create(
        self,
        *,
        customer_uuid: str,
        phone_number: str,
        app_realm: str | NotGiven = NOT_GIVEN,
        app_version: str | NotGiven = NOT_GIVEN,
        callback_url: str | NotGiven = NOT_GIVEN,
        device_id: str | NotGiven = NOT_GIVEN,
        device_model: str | NotGiven = NOT_GIVEN,
        device_type: Literal["IOS", "ANDROID", "WEB"] | NotGiven = NOT_GIVEN,
        ip: str | NotGiven = NOT_GIVEN,
        is_returning_user: bool | NotGiven = NOT_GIVEN,
        os_version: str | NotGiven = NOT_GIVEN,
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

          device_id: Unique identifier for the user's device. For Android, this corresponds to the
              `ANDROID_ID` and for iOS, this corresponds to the `identifierForVendor`.

          device_model: The model of the user's device.

          device_type: The type of device the user is using.

          ip: The IP address of the user's device.

          is_returning_user: Whether the user is a returning user on your app.

          os_version: The version of the user's device operating system.

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
                    "device_id": device_id,
                    "device_model": device_model,
                    "device_type": device_type,
                    "ip": ip,
                    "is_returning_user": is_returning_user,
                    "os_version": os_version,
                    "template_id": template_id,
                },
                authentication_create_params.AuthenticationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationCreateResponse,
        )


class AuthenticationWithRawResponse:
    def __init__(self, authentication: Authentication) -> None:
        self._authentication = authentication

        self.create = to_raw_response_wrapper(
            authentication.create,
        )

    @cached_property
    def feedback(self) -> FeedbackWithRawResponse:
        return FeedbackWithRawResponse(self._authentication.feedback)


class AsyncAuthenticationWithRawResponse:
    def __init__(self, authentication: AsyncAuthentication) -> None:
        self._authentication = authentication

        self.create = async_to_raw_response_wrapper(
            authentication.create,
        )

    @cached_property
    def feedback(self) -> AsyncFeedbackWithRawResponse:
        return AsyncFeedbackWithRawResponse(self._authentication.feedback)


class AuthenticationWithStreamingResponse:
    def __init__(self, authentication: Authentication) -> None:
        self._authentication = authentication

        self.create = to_streamed_response_wrapper(
            authentication.create,
        )

    @cached_property
    def feedback(self) -> FeedbackWithStreamingResponse:
        return FeedbackWithStreamingResponse(self._authentication.feedback)


class AsyncAuthenticationWithStreamingResponse:
    def __init__(self, authentication: AsyncAuthentication) -> None:
        self._authentication = authentication

        self.create = async_to_streamed_response_wrapper(
            authentication.create,
        )

    @cached_property
    def feedback(self) -> AsyncFeedbackWithStreamingResponse:
        return AsyncFeedbackWithStreamingResponse(self._authentication.feedback)
