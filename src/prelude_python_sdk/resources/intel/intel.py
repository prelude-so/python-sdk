# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .kyc import (
    KYCResource,
    AsyncKYCResource,
    KYCResourceWithRawResponse,
    AsyncKYCResourceWithRawResponse,
    KYCResourceWithStreamingResponse,
    AsyncKYCResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["IntelResource", "AsyncIntelResource"]


class IntelResource(SyncAPIResource):
    @cached_property
    def kyc(self) -> KYCResource:
        """
        Retrieve detailed information about a phone number including carrier data, line type, and portability status.
        """
        return KYCResource(self._client)

    @cached_property
    def with_raw_response(self) -> IntelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return IntelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IntelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return IntelResourceWithStreamingResponse(self)


class AsyncIntelResource(AsyncAPIResource):
    @cached_property
    def kyc(self) -> AsyncKYCResource:
        """
        Retrieve detailed information about a phone number including carrier data, line type, and portability status.
        """
        return AsyncKYCResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIntelResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncIntelResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIntelResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return AsyncIntelResourceWithStreamingResponse(self)


class IntelResourceWithRawResponse:
    def __init__(self, intel: IntelResource) -> None:
        self._intel = intel

    @cached_property
    def kyc(self) -> KYCResourceWithRawResponse:
        """
        Retrieve detailed information about a phone number including carrier data, line type, and portability status.
        """
        return KYCResourceWithRawResponse(self._intel.kyc)


class AsyncIntelResourceWithRawResponse:
    def __init__(self, intel: AsyncIntelResource) -> None:
        self._intel = intel

    @cached_property
    def kyc(self) -> AsyncKYCResourceWithRawResponse:
        """
        Retrieve detailed information about a phone number including carrier data, line type, and portability status.
        """
        return AsyncKYCResourceWithRawResponse(self._intel.kyc)


class IntelResourceWithStreamingResponse:
    def __init__(self, intel: IntelResource) -> None:
        self._intel = intel

    @cached_property
    def kyc(self) -> KYCResourceWithStreamingResponse:
        """
        Retrieve detailed information about a phone number including carrier data, line type, and portability status.
        """
        return KYCResourceWithStreamingResponse(self._intel.kyc)


class AsyncIntelResourceWithStreamingResponse:
    def __init__(self, intel: AsyncIntelResource) -> None:
        self._intel = intel

    @cached_property
    def kyc(self) -> AsyncKYCResourceWithStreamingResponse:
        """
        Retrieve detailed information about a phone number including carrier data, line type, and portability status.
        """
        return AsyncKYCResourceWithStreamingResponse(self._intel.kyc)
