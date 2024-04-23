# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from prelude import Prelude, AsyncPrelude
from tests.utils import assert_matches_type
from prelude.types import CheckCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCheck:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Prelude) -> None:
        check = client.check.create(
            authentication_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            check_code="123456",
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CheckCreateResponse, check, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Prelude) -> None:
        response = client.check.with_raw_response.create(
            authentication_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            check_code="123456",
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = response.parse()
        assert_matches_type(CheckCreateResponse, check, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Prelude) -> None:
        with client.check.with_streaming_response.create(
            authentication_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            check_code="123456",
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = response.parse()
            assert_matches_type(CheckCreateResponse, check, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCheck:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPrelude) -> None:
        check = await async_client.check.create(
            authentication_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            check_code="123456",
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CheckCreateResponse, check, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrelude) -> None:
        response = await async_client.check.with_raw_response.create(
            authentication_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            check_code="123456",
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        check = await response.parse()
        assert_matches_type(CheckCreateResponse, check, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrelude) -> None:
        async with async_client.check.with_streaming_response.create(
            authentication_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            check_code="123456",
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            check = await response.parse()
            assert_matches_type(CheckCreateResponse, check, path=["response"])

        assert cast(Any, response.is_closed) is True
