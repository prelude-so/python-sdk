# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prelude_python_sdk import Prelude, AsyncPrelude
from prelude_python_sdk.types import LookupLookupResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLookup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_lookup(self, client: Prelude) -> None:
        lookup = client.lookup.lookup(
            phone_number="+12065550100",
        )
        assert_matches_type(LookupLookupResponse, lookup, path=["response"])

    @parametrize
    def test_method_lookup_with_all_params(self, client: Prelude) -> None:
        lookup = client.lookup.lookup(
            phone_number="+12065550100",
            type=["cnam"],
        )
        assert_matches_type(LookupLookupResponse, lookup, path=["response"])

    @parametrize
    def test_raw_response_lookup(self, client: Prelude) -> None:
        response = client.lookup.with_raw_response.lookup(
            phone_number="+12065550100",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lookup = response.parse()
        assert_matches_type(LookupLookupResponse, lookup, path=["response"])

    @parametrize
    def test_streaming_response_lookup(self, client: Prelude) -> None:
        with client.lookup.with_streaming_response.lookup(
            phone_number="+12065550100",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lookup = response.parse()
            assert_matches_type(LookupLookupResponse, lookup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_lookup(self, client: Prelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.lookup.with_raw_response.lookup(
                phone_number="",
            )


class TestAsyncLookup:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_lookup(self, async_client: AsyncPrelude) -> None:
        lookup = await async_client.lookup.lookup(
            phone_number="+12065550100",
        )
        assert_matches_type(LookupLookupResponse, lookup, path=["response"])

    @parametrize
    async def test_method_lookup_with_all_params(self, async_client: AsyncPrelude) -> None:
        lookup = await async_client.lookup.lookup(
            phone_number="+12065550100",
            type=["cnam"],
        )
        assert_matches_type(LookupLookupResponse, lookup, path=["response"])

    @parametrize
    async def test_raw_response_lookup(self, async_client: AsyncPrelude) -> None:
        response = await async_client.lookup.with_raw_response.lookup(
            phone_number="+12065550100",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lookup = await response.parse()
        assert_matches_type(LookupLookupResponse, lookup, path=["response"])

    @parametrize
    async def test_streaming_response_lookup(self, async_client: AsyncPrelude) -> None:
        async with async_client.lookup.with_streaming_response.lookup(
            phone_number="+12065550100",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lookup = await response.parse()
            assert_matches_type(LookupLookupResponse, lookup, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_lookup(self, async_client: AsyncPrelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.lookup.with_raw_response.lookup(
                phone_number="",
            )
