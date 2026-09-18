# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.intel import kyc_match_params
from ..._base_client import make_request_options
from ...types.intel.kyc_match_response import KYCMatchResponse

__all__ = ["KYCResource", "AsyncKYCResource"]


class KYCResource(SyncAPIResource):
    """
    Retrieve detailed information about a phone number including carrier data, line type, and portability status.
    """

    @cached_property
    def with_raw_response(self) -> KYCResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return KYCResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KYCResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return KYCResourceWithStreamingResponse(self)

    def match(
        self,
        phone: str,
        *,
        address: str | Omit = omit,
        birthdate: Union[str, date] | Omit = omit,
        country: str | Omit = omit,
        email: str | Omit = omit,
        family_name: str | Omit = omit,
        given_name: str | Omit = omit,
        locality: str | Omit = omit,
        postal_code: str | Omit = omit,
        region: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYCMatchResponse:
        """
        Verify identity attributes against the subscriber record held by the end-user's
        mobile operator. Send a phone number along with the attributes to check; Prelude
        resolves the operator internally and returns a per-attribute match. Currently
        available for France only (Orange, SFR, Bouygues) and must be enabled for your
        account.

        Args:
          phone: An E.164 formatted phone number whose subscriber identity to match against.

          address: The street address.

          birthdate: The date of birth in ISO 8601 (`YYYY-MM-DD`) format. Compared exactly.

          country: The ISO 3166-1 alpha-2 country code. Compared exactly.

          email: The email address.

          family_name: The end-user's family (last) name.

          given_name: The end-user's given (first) name.

          locality: The locality (city).

          postal_code: The postal code. Compared exactly.

          region: The region, state, or province.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone:
            raise ValueError(f"Expected a non-empty value for `phone` but received {phone!r}")
        return self._post(
            path_template("/v2/intel/kyc/match/{phone}", phone=phone),
            body=maybe_transform(
                {
                    "address": address,
                    "birthdate": birthdate,
                    "country": country,
                    "email": email,
                    "family_name": family_name,
                    "given_name": given_name,
                    "locality": locality,
                    "postal_code": postal_code,
                    "region": region,
                },
                kyc_match_params.KYCMatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYCMatchResponse,
        )


class AsyncKYCResource(AsyncAPIResource):
    """
    Retrieve detailed information about a phone number including carrier data, line type, and portability status.
    """

    @cached_property
    def with_raw_response(self) -> AsyncKYCResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/prelude-so/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncKYCResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKYCResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/prelude-so/python-sdk#with_streaming_response
        """
        return AsyncKYCResourceWithStreamingResponse(self)

    async def match(
        self,
        phone: str,
        *,
        address: str | Omit = omit,
        birthdate: Union[str, date] | Omit = omit,
        country: str | Omit = omit,
        email: str | Omit = omit,
        family_name: str | Omit = omit,
        given_name: str | Omit = omit,
        locality: str | Omit = omit,
        postal_code: str | Omit = omit,
        region: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYCMatchResponse:
        """
        Verify identity attributes against the subscriber record held by the end-user's
        mobile operator. Send a phone number along with the attributes to check; Prelude
        resolves the operator internally and returns a per-attribute match. Currently
        available for France only (Orange, SFR, Bouygues) and must be enabled for your
        account.

        Args:
          phone: An E.164 formatted phone number whose subscriber identity to match against.

          address: The street address.

          birthdate: The date of birth in ISO 8601 (`YYYY-MM-DD`) format. Compared exactly.

          country: The ISO 3166-1 alpha-2 country code. Compared exactly.

          email: The email address.

          family_name: The end-user's family (last) name.

          given_name: The end-user's given (first) name.

          locality: The locality (city).

          postal_code: The postal code. Compared exactly.

          region: The region, state, or province.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone:
            raise ValueError(f"Expected a non-empty value for `phone` but received {phone!r}")
        return await self._post(
            path_template("/v2/intel/kyc/match/{phone}", phone=phone),
            body=await async_maybe_transform(
                {
                    "address": address,
                    "birthdate": birthdate,
                    "country": country,
                    "email": email,
                    "family_name": family_name,
                    "given_name": given_name,
                    "locality": locality,
                    "postal_code": postal_code,
                    "region": region,
                },
                kyc_match_params.KYCMatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYCMatchResponse,
        )


class KYCResourceWithRawResponse:
    def __init__(self, kyc: KYCResource) -> None:
        self._kyc = kyc

        self.match = to_raw_response_wrapper(
            kyc.match,
        )


class AsyncKYCResourceWithRawResponse:
    def __init__(self, kyc: AsyncKYCResource) -> None:
        self._kyc = kyc

        self.match = async_to_raw_response_wrapper(
            kyc.match,
        )


class KYCResourceWithStreamingResponse:
    def __init__(self, kyc: KYCResource) -> None:
        self._kyc = kyc

        self.match = to_streamed_response_wrapper(
            kyc.match,
        )


class AsyncKYCResourceWithStreamingResponse:
    def __init__(self, kyc: AsyncKYCResource) -> None:
        self._kyc = kyc

        self.match = async_to_streamed_response_wrapper(
            kyc.match,
        )
