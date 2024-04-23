# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from prelude import Prelude, AsyncPrelude
from tests.utils import assert_matches_type
from prelude.types import RetryCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Prelude) -> None:
        retry = client.retry.create(
            authentication_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RetryCreateResponse, retry, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Prelude) -> None:
        response = client.retry.with_raw_response.create(
            authentication_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retry = response.parse()
        assert_matches_type(RetryCreateResponse, retry, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Prelude) -> None:
        with client.retry.with_streaming_response.create(
            authentication_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retry = response.parse()
            assert_matches_type(RetryCreateResponse, retry, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRetry:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPrelude) -> None:
        retry = await async_client.retry.create(
            authentication_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RetryCreateResponse, retry, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrelude) -> None:
        response = await async_client.retry.with_raw_response.create(
            authentication_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retry = await response.parse()
        assert_matches_type(RetryCreateResponse, retry, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrelude) -> None:
        async with async_client.retry.with_streaming_response.create(
            authentication_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retry = await response.parse()
            assert_matches_type(RetryCreateResponse, retry, path=["response"])

        assert cast(Any, response.is_closed) is True
