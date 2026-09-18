# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prelude_python_sdk import Prelude, AsyncPrelude
from prelude_python_sdk._utils import parse_datetime
from prelude_python_sdk.types.verification.phone import (
    HistoryListResponse,
    HistoryRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHistory:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Prelude) -> None:
        history = client.verification.phone.history.retrieve(
            "vrf_01jc0t6fwwfgfsq1md24mhyztj",
        )
        assert_matches_type(HistoryRetrieveResponse, history, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Prelude) -> None:
        response = client.verification.phone.history.with_raw_response.retrieve(
            "vrf_01jc0t6fwwfgfsq1md24mhyztj",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(HistoryRetrieveResponse, history, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Prelude) -> None:
        with client.verification.phone.history.with_streaming_response.retrieve(
            "vrf_01jc0t6fwwfgfsq1md24mhyztj",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(HistoryRetrieveResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Prelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.verification.phone.history.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_list(self, client: Prelude) -> None:
        history = client.verification.phone.history.list()
        assert_matches_type(HistoryListResponse, history, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Prelude) -> None:
        history = client.verification.phone.history.list(
            channels=["sms"],
            cursor="cursor",
            device_platform="android",
            from_=parse_datetime("2026-09-01T00:00:00Z"),
            limit=1,
            max_attempts=0,
            min_attempts=0,
            phone_number="+33612345678",
            region="FR",
            status="converted",
            template_id="template_01jc0t6fwwfgfsq1md24mhyztj",
            to=parse_datetime("2026-09-08T00:00:00Z"),
        )
        assert_matches_type(HistoryListResponse, history, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Prelude) -> None:
        response = client.verification.phone.history.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = response.parse()
        assert_matches_type(HistoryListResponse, history, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Prelude) -> None:
        with client.verification.phone.history.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = response.parse()
            assert_matches_type(HistoryListResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHistory:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPrelude) -> None:
        history = await async_client.verification.phone.history.retrieve(
            "vrf_01jc0t6fwwfgfsq1md24mhyztj",
        )
        assert_matches_type(HistoryRetrieveResponse, history, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPrelude) -> None:
        response = await async_client.verification.phone.history.with_raw_response.retrieve(
            "vrf_01jc0t6fwwfgfsq1md24mhyztj",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(HistoryRetrieveResponse, history, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPrelude) -> None:
        async with async_client.verification.phone.history.with_streaming_response.retrieve(
            "vrf_01jc0t6fwwfgfsq1md24mhyztj",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(HistoryRetrieveResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPrelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.verification.phone.history.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPrelude) -> None:
        history = await async_client.verification.phone.history.list()
        assert_matches_type(HistoryListResponse, history, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPrelude) -> None:
        history = await async_client.verification.phone.history.list(
            channels=["sms"],
            cursor="cursor",
            device_platform="android",
            from_=parse_datetime("2026-09-01T00:00:00Z"),
            limit=1,
            max_attempts=0,
            min_attempts=0,
            phone_number="+33612345678",
            region="FR",
            status="converted",
            template_id="template_01jc0t6fwwfgfsq1md24mhyztj",
            to=parse_datetime("2026-09-08T00:00:00Z"),
        )
        assert_matches_type(HistoryListResponse, history, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPrelude) -> None:
        response = await async_client.verification.phone.history.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        history = await response.parse()
        assert_matches_type(HistoryListResponse, history, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPrelude) -> None:
        async with async_client.verification.phone.history.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            history = await response.parse()
            assert_matches_type(HistoryListResponse, history, path=["response"])

        assert cast(Any, response.is_closed) is True
