# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import PreludeError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Prelude",
    "AsyncPrelude",
    "Client",
    "AsyncClient",
]


class Prelude(SyncAPIClient):
    authentication: resources.AuthenticationResource
    check: resources.CheckResource
    retry: resources.RetryResource
    lookup: resources.LookupResource
    with_raw_response: PreludeWithRawResponse
    with_streaming_response: PreludeWithStreamedResponse

    # client options
    api_key: str
    customer_uuid: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        customer_uuid: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous prelude client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `PRELUDE_API_KEY`
        - `customer_uuid` from `PRELUDE_CUSTOMER_UUID`
        """
        if api_key is None:
            api_key = os.environ.get("PRELUDE_API_KEY")
        if api_key is None:
            raise PreludeError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PRELUDE_API_KEY environment variable"
            )
        self.api_key = api_key

        if customer_uuid is None:
            customer_uuid = os.environ.get("PRELUDE_CUSTOMER_UUID")
        if customer_uuid is None:
            raise PreludeError(
                "The customer_uuid client option must be set either by passing customer_uuid to the client or by setting the PRELUDE_CUSTOMER_UUID environment variable"
            )
        self.customer_uuid = customer_uuid

        if base_url is None:
            base_url = os.environ.get("PRELUDE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.ding.live/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.authentication = resources.AuthenticationResource(self)
        self.check = resources.CheckResource(self)
        self.retry = resources.RetryResource(self)
        self.lookup = resources.LookupResource(self)
        self.with_raw_response = PreludeWithRawResponse(self)
        self.with_streaming_response = PreludeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            "CUSTOMER_UUID": self.customer_uuid,
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        customer_uuid: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            customer_uuid=customer_uuid or self.customer_uuid,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncPrelude(AsyncAPIClient):
    authentication: resources.AsyncAuthenticationResource
    check: resources.AsyncCheckResource
    retry: resources.AsyncRetryResource
    lookup: resources.AsyncLookupResource
    with_raw_response: AsyncPreludeWithRawResponse
    with_streaming_response: AsyncPreludeWithStreamedResponse

    # client options
    api_key: str
    customer_uuid: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        customer_uuid: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async prelude client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `api_key` from `PRELUDE_API_KEY`
        - `customer_uuid` from `PRELUDE_CUSTOMER_UUID`
        """
        if api_key is None:
            api_key = os.environ.get("PRELUDE_API_KEY")
        if api_key is None:
            raise PreludeError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PRELUDE_API_KEY environment variable"
            )
        self.api_key = api_key

        if customer_uuid is None:
            customer_uuid = os.environ.get("PRELUDE_CUSTOMER_UUID")
        if customer_uuid is None:
            raise PreludeError(
                "The customer_uuid client option must be set either by passing customer_uuid to the client or by setting the PRELUDE_CUSTOMER_UUID environment variable"
            )
        self.customer_uuid = customer_uuid

        if base_url is None:
            base_url = os.environ.get("PRELUDE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.ding.live/v1"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.authentication = resources.AsyncAuthenticationResource(self)
        self.check = resources.AsyncCheckResource(self)
        self.retry = resources.AsyncRetryResource(self)
        self.lookup = resources.AsyncLookupResource(self)
        self.with_raw_response = AsyncPreludeWithRawResponse(self)
        self.with_streaming_response = AsyncPreludeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"x-api-key": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            "CUSTOMER_UUID": self.customer_uuid,
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        customer_uuid: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            customer_uuid=customer_uuid or self.customer_uuid,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class PreludeWithRawResponse:
    def __init__(self, client: Prelude) -> None:
        self.authentication = resources.AuthenticationResourceWithRawResponse(client.authentication)
        self.check = resources.CheckResourceWithRawResponse(client.check)
        self.retry = resources.RetryResourceWithRawResponse(client.retry)
        self.lookup = resources.LookupResourceWithRawResponse(client.lookup)


class AsyncPreludeWithRawResponse:
    def __init__(self, client: AsyncPrelude) -> None:
        self.authentication = resources.AsyncAuthenticationResourceWithRawResponse(client.authentication)
        self.check = resources.AsyncCheckResourceWithRawResponse(client.check)
        self.retry = resources.AsyncRetryResourceWithRawResponse(client.retry)
        self.lookup = resources.AsyncLookupResourceWithRawResponse(client.lookup)


class PreludeWithStreamedResponse:
    def __init__(self, client: Prelude) -> None:
        self.authentication = resources.AuthenticationResourceWithStreamingResponse(client.authentication)
        self.check = resources.CheckResourceWithStreamingResponse(client.check)
        self.retry = resources.RetryResourceWithStreamingResponse(client.retry)
        self.lookup = resources.LookupResourceWithStreamingResponse(client.lookup)


class AsyncPreludeWithStreamedResponse:
    def __init__(self, client: AsyncPrelude) -> None:
        self.authentication = resources.AsyncAuthenticationResourceWithStreamingResponse(client.authentication)
        self.check = resources.AsyncCheckResourceWithStreamingResponse(client.check)
        self.retry = resources.AsyncRetryResourceWithStreamingResponse(client.retry)
        self.lookup = resources.AsyncLookupResourceWithStreamingResponse(client.lookup)


Client = Prelude

AsyncClient = AsyncPrelude
