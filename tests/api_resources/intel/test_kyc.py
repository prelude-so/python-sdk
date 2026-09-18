# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prelude_python_sdk import Prelude, AsyncPrelude
from prelude_python_sdk._utils import parse_date
from prelude_python_sdk.types.intel import KYCMatchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKYC:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_match(self, client: Prelude) -> None:
        kyc = client.intel.kyc.match(
            phone="+12065550100",
        )
        assert_matches_type(KYCMatchResponse, kyc, path=["response"])

    @parametrize
    def test_method_match_with_all_params(self, client: Prelude) -> None:
        kyc = client.intel.kyc.match(
            phone="+12065550100",
            address="12 rue de la Paix",
            birthdate=parse_date("1990-01-15"),
            country="FR",
            email="jean.dupont@example.com",
            family_name="Dupont",
            given_name="Jean",
            locality="Paris",
            postal_code="75002",
            region="Île-de-France",
        )
        assert_matches_type(KYCMatchResponse, kyc, path=["response"])

    @parametrize
    def test_raw_response_match(self, client: Prelude) -> None:
        response = client.intel.kyc.with_raw_response.match(
            phone="+12065550100",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(KYCMatchResponse, kyc, path=["response"])

    @parametrize
    def test_streaming_response_match(self, client: Prelude) -> None:
        with client.intel.kyc.with_streaming_response.match(
            phone="+12065550100",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(KYCMatchResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_match(self, client: Prelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone` but received ''"):
            client.intel.kyc.with_raw_response.match(
                phone="",
            )


class TestAsyncKYC:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_match(self, async_client: AsyncPrelude) -> None:
        kyc = await async_client.intel.kyc.match(
            phone="+12065550100",
        )
        assert_matches_type(KYCMatchResponse, kyc, path=["response"])

    @parametrize
    async def test_method_match_with_all_params(self, async_client: AsyncPrelude) -> None:
        kyc = await async_client.intel.kyc.match(
            phone="+12065550100",
            address="12 rue de la Paix",
            birthdate=parse_date("1990-01-15"),
            country="FR",
            email="jean.dupont@example.com",
            family_name="Dupont",
            given_name="Jean",
            locality="Paris",
            postal_code="75002",
            region="Île-de-France",
        )
        assert_matches_type(KYCMatchResponse, kyc, path=["response"])

    @parametrize
    async def test_raw_response_match(self, async_client: AsyncPrelude) -> None:
        response = await async_client.intel.kyc.with_raw_response.match(
            phone="+12065550100",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(KYCMatchResponse, kyc, path=["response"])

    @parametrize
    async def test_streaming_response_match(self, async_client: AsyncPrelude) -> None:
        async with async_client.intel.kyc.with_streaming_response.match(
            phone="+12065550100",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(KYCMatchResponse, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_match(self, async_client: AsyncPrelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone` but received ''"):
            await async_client.intel.kyc.with_raw_response.match(
                phone="",
            )
