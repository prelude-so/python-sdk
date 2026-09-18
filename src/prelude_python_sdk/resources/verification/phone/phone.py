# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .history import (
    HistoryResource,
    AsyncHistoryResource,
    HistoryResourceWithRawResponse,
    AsyncHistoryResourceWithRawResponse,
    HistoryResourceWithStreamingResponse,
    AsyncHistoryResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PhoneResource", "AsyncPhoneResource"]


class PhoneResource(SyncAPIResource):
    @cached_property
    def history(self) -> HistoryResource:
        """Verify phone numbers."""
        return HistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> PhoneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return PhoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return PhoneResourceWithStreamingResponse(self)


class AsyncPhoneResource(AsyncAPIResource):
    @cached_property
    def history(self) -> AsyncHistoryResource:
        """Verify phone numbers."""
        return AsyncHistoryResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPhoneResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return AsyncPhoneResourceWithStreamingResponse(self)


class PhoneResourceWithRawResponse:
    def __init__(self, phone: PhoneResource) -> None:
        self._phone = phone

    @cached_property
    def history(self) -> HistoryResourceWithRawResponse:
        """Verify phone numbers."""
        return HistoryResourceWithRawResponse(self._phone.history)


class AsyncPhoneResourceWithRawResponse:
    def __init__(self, phone: AsyncPhoneResource) -> None:
        self._phone = phone

    @cached_property
    def history(self) -> AsyncHistoryResourceWithRawResponse:
        """Verify phone numbers."""
        return AsyncHistoryResourceWithRawResponse(self._phone.history)


class PhoneResourceWithStreamingResponse:
    def __init__(self, phone: PhoneResource) -> None:
        self._phone = phone

    @cached_property
    def history(self) -> HistoryResourceWithStreamingResponse:
        """Verify phone numbers."""
        return HistoryResourceWithStreamingResponse(self._phone.history)


class AsyncPhoneResourceWithStreamingResponse:
    def __init__(self, phone: AsyncPhoneResource) -> None:
        self._phone = phone

    @cached_property
    def history(self) -> AsyncHistoryResourceWithStreamingResponse:
        """Verify phone numbers."""
        return AsyncHistoryResourceWithStreamingResponse(self._phone.history)
