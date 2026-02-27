# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import PreludeError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import watch, lookup, notify, verification, transactional, verification_management
    from .resources.watch import WatchResource, AsyncWatchResource
    from .resources.lookup import LookupResource, AsyncLookupResource
    from .resources.notify import NotifyResource, AsyncNotifyResource
    from .resources.verification import VerificationResource, AsyncVerificationResource
    from .resources.transactional import TransactionalResource, AsyncTransactionalResource
    from .resources.verification_management import VerificationManagementResource, AsyncVerificationManagementResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Prelude", "AsyncPrelude", "Client", "AsyncClient"]


class Prelude(SyncAPIClient):
    # client options
    api_token: str

    def __init__(
        self,
        *,
        api_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new synchronous Prelude client instance.

        This automatically infers the `api_token` argument from the `API_TOKEN` environment variable if it is not provided.
        """
        if api_token is None:
            api_token = os.environ.get("API_TOKEN")
        if api_token is None:
            raise PreludeError(
                "The api_token client option must be set either by passing api_token to the client or by setting the API_TOKEN environment variable"
            )
        self.api_token = api_token

        if base_url is None:
            base_url = os.environ.get("PRELUDE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.prelude.dev"

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

    @cached_property
    def lookup(self) -> LookupResource:
        """
        Retrieve detailed information about a phone number including carrier data, line type, and portability status.
        """
        from .resources.lookup import LookupResource

        return LookupResource(self)

    @cached_property
    def notify(self) -> NotifyResource:
        """Send transactional and marketing messages with compliance enforcement."""
        from .resources.notify import NotifyResource

        return NotifyResource(self)

    @cached_property
    def transactional(self) -> TransactionalResource:
        """Send transactional messages (deprecated - use Notify API instead)."""
        from .resources.transactional import TransactionalResource

        return TransactionalResource(self)

    @cached_property
    def verification(self) -> VerificationResource:
        """Verify phone numbers."""
        from .resources.verification import VerificationResource

        return VerificationResource(self)

    @cached_property
    def verification_management(self) -> VerificationManagementResource:
        """Verify phone numbers."""
        from .resources.verification_management import VerificationManagementResource

        return VerificationManagementResource(self)

    @cached_property
    def watch(self) -> WatchResource:
        """Evaluate email addresses and phone numbers for trustworthiness."""
        from .resources.watch import WatchResource

        return WatchResource(self)

    @cached_property
    def with_raw_response(self) -> PreludeWithRawResponse:
        return PreludeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreludeWithStreamedResponse:
        return PreludeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_token = self.api_token
        return {"Authorization": f"Bearer {api_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
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
            api_token=api_token or self.api_token,
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
    # client options
    api_token: str

    def __init__(
        self,
        *,
        api_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
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
        """Construct a new async AsyncPrelude client instance.

        This automatically infers the `api_token` argument from the `API_TOKEN` environment variable if it is not provided.
        """
        if api_token is None:
            api_token = os.environ.get("API_TOKEN")
        if api_token is None:
            raise PreludeError(
                "The api_token client option must be set either by passing api_token to the client or by setting the API_TOKEN environment variable"
            )
        self.api_token = api_token

        if base_url is None:
            base_url = os.environ.get("PRELUDE_BASE_URL")
        if base_url is None:
            base_url = f"https://api.prelude.dev"

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

    @cached_property
    def lookup(self) -> AsyncLookupResource:
        """
        Retrieve detailed information about a phone number including carrier data, line type, and portability status.
        """
        from .resources.lookup import AsyncLookupResource

        return AsyncLookupResource(self)

    @cached_property
    def notify(self) -> AsyncNotifyResource:
        """Send transactional and marketing messages with compliance enforcement."""
        from .resources.notify import AsyncNotifyResource

        return AsyncNotifyResource(self)

    @cached_property
    def transactional(self) -> AsyncTransactionalResource:
        """Send transactional messages (deprecated - use Notify API instead)."""
        from .resources.transactional import AsyncTransactionalResource

        return AsyncTransactionalResource(self)

    @cached_property
    def verification(self) -> AsyncVerificationResource:
        """Verify phone numbers."""
        from .resources.verification import AsyncVerificationResource

        return AsyncVerificationResource(self)

    @cached_property
    def verification_management(self) -> AsyncVerificationManagementResource:
        """Verify phone numbers."""
        from .resources.verification_management import AsyncVerificationManagementResource

        return AsyncVerificationManagementResource(self)

    @cached_property
    def watch(self) -> AsyncWatchResource:
        """Evaluate email addresses and phone numbers for trustworthiness."""
        from .resources.watch import AsyncWatchResource

        return AsyncWatchResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncPreludeWithRawResponse:
        return AsyncPreludeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreludeWithStreamedResponse:
        return AsyncPreludeWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_token = self.api_token
        return {"Authorization": f"Bearer {api_token}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
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
            api_token=api_token or self.api_token,
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
    _client: Prelude

    def __init__(self, client: Prelude) -> None:
        self._client = client

    @cached_property
    def lookup(self) -> lookup.LookupResourceWithRawResponse:
        """
        Retrieve detailed information about a phone number including carrier data, line type, and portability status.
        """
        from .resources.lookup import LookupResourceWithRawResponse

        return LookupResourceWithRawResponse(self._client.lookup)

    @cached_property
    def notify(self) -> notify.NotifyResourceWithRawResponse:
        """Send transactional and marketing messages with compliance enforcement."""
        from .resources.notify import NotifyResourceWithRawResponse

        return NotifyResourceWithRawResponse(self._client.notify)

    @cached_property
    def transactional(self) -> transactional.TransactionalResourceWithRawResponse:
        """Send transactional messages (deprecated - use Notify API instead)."""
        from .resources.transactional import TransactionalResourceWithRawResponse

        return TransactionalResourceWithRawResponse(self._client.transactional)

    @cached_property
    def verification(self) -> verification.VerificationResourceWithRawResponse:
        """Verify phone numbers."""
        from .resources.verification import VerificationResourceWithRawResponse

        return VerificationResourceWithRawResponse(self._client.verification)

    @cached_property
    def verification_management(self) -> verification_management.VerificationManagementResourceWithRawResponse:
        """Verify phone numbers."""
        from .resources.verification_management import VerificationManagementResourceWithRawResponse

        return VerificationManagementResourceWithRawResponse(self._client.verification_management)

    @cached_property
    def watch(self) -> watch.WatchResourceWithRawResponse:
        """Evaluate email addresses and phone numbers for trustworthiness."""
        from .resources.watch import WatchResourceWithRawResponse

        return WatchResourceWithRawResponse(self._client.watch)


class AsyncPreludeWithRawResponse:
    _client: AsyncPrelude

    def __init__(self, client: AsyncPrelude) -> None:
        self._client = client

    @cached_property
    def lookup(self) -> lookup.AsyncLookupResourceWithRawResponse:
        """
        Retrieve detailed information about a phone number including carrier data, line type, and portability status.
        """
        from .resources.lookup import AsyncLookupResourceWithRawResponse

        return AsyncLookupResourceWithRawResponse(self._client.lookup)

    @cached_property
    def notify(self) -> notify.AsyncNotifyResourceWithRawResponse:
        """Send transactional and marketing messages with compliance enforcement."""
        from .resources.notify import AsyncNotifyResourceWithRawResponse

        return AsyncNotifyResourceWithRawResponse(self._client.notify)

    @cached_property
    def transactional(self) -> transactional.AsyncTransactionalResourceWithRawResponse:
        """Send transactional messages (deprecated - use Notify API instead)."""
        from .resources.transactional import AsyncTransactionalResourceWithRawResponse

        return AsyncTransactionalResourceWithRawResponse(self._client.transactional)

    @cached_property
    def verification(self) -> verification.AsyncVerificationResourceWithRawResponse:
        """Verify phone numbers."""
        from .resources.verification import AsyncVerificationResourceWithRawResponse

        return AsyncVerificationResourceWithRawResponse(self._client.verification)

    @cached_property
    def verification_management(self) -> verification_management.AsyncVerificationManagementResourceWithRawResponse:
        """Verify phone numbers."""
        from .resources.verification_management import AsyncVerificationManagementResourceWithRawResponse

        return AsyncVerificationManagementResourceWithRawResponse(self._client.verification_management)

    @cached_property
    def watch(self) -> watch.AsyncWatchResourceWithRawResponse:
        """Evaluate email addresses and phone numbers for trustworthiness."""
        from .resources.watch import AsyncWatchResourceWithRawResponse

        return AsyncWatchResourceWithRawResponse(self._client.watch)


class PreludeWithStreamedResponse:
    _client: Prelude

    def __init__(self, client: Prelude) -> None:
        self._client = client

    @cached_property
    def lookup(self) -> lookup.LookupResourceWithStreamingResponse:
        """
        Retrieve detailed information about a phone number including carrier data, line type, and portability status.
        """
        from .resources.lookup import LookupResourceWithStreamingResponse

        return LookupResourceWithStreamingResponse(self._client.lookup)

    @cached_property
    def notify(self) -> notify.NotifyResourceWithStreamingResponse:
        """Send transactional and marketing messages with compliance enforcement."""
        from .resources.notify import NotifyResourceWithStreamingResponse

        return NotifyResourceWithStreamingResponse(self._client.notify)

    @cached_property
    def transactional(self) -> transactional.TransactionalResourceWithStreamingResponse:
        """Send transactional messages (deprecated - use Notify API instead)."""
        from .resources.transactional import TransactionalResourceWithStreamingResponse

        return TransactionalResourceWithStreamingResponse(self._client.transactional)

    @cached_property
    def verification(self) -> verification.VerificationResourceWithStreamingResponse:
        """Verify phone numbers."""
        from .resources.verification import VerificationResourceWithStreamingResponse

        return VerificationResourceWithStreamingResponse(self._client.verification)

    @cached_property
    def verification_management(self) -> verification_management.VerificationManagementResourceWithStreamingResponse:
        """Verify phone numbers."""
        from .resources.verification_management import VerificationManagementResourceWithStreamingResponse

        return VerificationManagementResourceWithStreamingResponse(self._client.verification_management)

    @cached_property
    def watch(self) -> watch.WatchResourceWithStreamingResponse:
        """Evaluate email addresses and phone numbers for trustworthiness."""
        from .resources.watch import WatchResourceWithStreamingResponse

        return WatchResourceWithStreamingResponse(self._client.watch)


class AsyncPreludeWithStreamedResponse:
    _client: AsyncPrelude

    def __init__(self, client: AsyncPrelude) -> None:
        self._client = client

    @cached_property
    def lookup(self) -> lookup.AsyncLookupResourceWithStreamingResponse:
        """
        Retrieve detailed information about a phone number including carrier data, line type, and portability status.
        """
        from .resources.lookup import AsyncLookupResourceWithStreamingResponse

        return AsyncLookupResourceWithStreamingResponse(self._client.lookup)

    @cached_property
    def notify(self) -> notify.AsyncNotifyResourceWithStreamingResponse:
        """Send transactional and marketing messages with compliance enforcement."""
        from .resources.notify import AsyncNotifyResourceWithStreamingResponse

        return AsyncNotifyResourceWithStreamingResponse(self._client.notify)

    @cached_property
    def transactional(self) -> transactional.AsyncTransactionalResourceWithStreamingResponse:
        """Send transactional messages (deprecated - use Notify API instead)."""
        from .resources.transactional import AsyncTransactionalResourceWithStreamingResponse

        return AsyncTransactionalResourceWithStreamingResponse(self._client.transactional)

    @cached_property
    def verification(self) -> verification.AsyncVerificationResourceWithStreamingResponse:
        """Verify phone numbers."""
        from .resources.verification import AsyncVerificationResourceWithStreamingResponse

        return AsyncVerificationResourceWithStreamingResponse(self._client.verification)

    @cached_property
    def verification_management(
        self,
    ) -> verification_management.AsyncVerificationManagementResourceWithStreamingResponse:
        """Verify phone numbers."""
        from .resources.verification_management import AsyncVerificationManagementResourceWithStreamingResponse

        return AsyncVerificationManagementResourceWithStreamingResponse(self._client.verification_management)

    @cached_property
    def watch(self) -> watch.AsyncWatchResourceWithStreamingResponse:
        """Evaluate email addresses and phone numbers for trustworthiness."""
        from .resources.watch import AsyncWatchResourceWithStreamingResponse

        return AsyncWatchResourceWithStreamingResponse(self._client.watch)


Client = Prelude

AsyncClient = AsyncPrelude
