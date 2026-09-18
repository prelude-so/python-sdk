# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prelude_python_sdk import Prelude, AsyncPrelude
from prelude_python_sdk.types.verification_management import (
    SandboxAddPhoneNumberResponse,
    SandboxListPhoneNumbersResponse,
    SandboxDeletePhoneNumberResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSandbox:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_add_phone_number(self, client: Prelude) -> None:
        sandbox = client.verification_management.sandbox.add_phone_number(
            attempt_code="123456",
            phone_number="+30123456789",
        )
        assert_matches_type(SandboxAddPhoneNumberResponse, sandbox, path=["response"])

    @parametrize
    def test_raw_response_add_phone_number(self, client: Prelude) -> None:
        response = client.verification_management.sandbox.with_raw_response.add_phone_number(
            attempt_code="123456",
            phone_number="+30123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxAddPhoneNumberResponse, sandbox, path=["response"])

    @parametrize
    def test_streaming_response_add_phone_number(self, client: Prelude) -> None:
        with client.verification_management.sandbox.with_streaming_response.add_phone_number(
            attempt_code="123456",
            phone_number="+30123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxAddPhoneNumberResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete_phone_number(self, client: Prelude) -> None:
        sandbox = client.verification_management.sandbox.delete_phone_number(
            "+12065550100",
        )
        assert_matches_type(SandboxDeletePhoneNumberResponse, sandbox, path=["response"])

    @parametrize
    def test_raw_response_delete_phone_number(self, client: Prelude) -> None:
        response = client.verification_management.sandbox.with_raw_response.delete_phone_number(
            "+12065550100",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxDeletePhoneNumberResponse, sandbox, path=["response"])

    @parametrize
    def test_streaming_response_delete_phone_number(self, client: Prelude) -> None:
        with client.verification_management.sandbox.with_streaming_response.delete_phone_number(
            "+12065550100",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxDeletePhoneNumberResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete_phone_number(self, client: Prelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.verification_management.sandbox.with_raw_response.delete_phone_number(
                "",
            )

    @parametrize
    def test_method_list_phone_numbers(self, client: Prelude) -> None:
        sandbox = client.verification_management.sandbox.list_phone_numbers()
        assert_matches_type(SandboxListPhoneNumbersResponse, sandbox, path=["response"])

    @parametrize
    def test_raw_response_list_phone_numbers(self, client: Prelude) -> None:
        response = client.verification_management.sandbox.with_raw_response.list_phone_numbers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxListPhoneNumbersResponse, sandbox, path=["response"])

    @parametrize
    def test_streaming_response_list_phone_numbers(self, client: Prelude) -> None:
        with client.verification_management.sandbox.with_streaming_response.list_phone_numbers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxListPhoneNumbersResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSandbox:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_add_phone_number(self, async_client: AsyncPrelude) -> None:
        sandbox = await async_client.verification_management.sandbox.add_phone_number(
            attempt_code="123456",
            phone_number="+30123456789",
        )
        assert_matches_type(SandboxAddPhoneNumberResponse, sandbox, path=["response"])

    @parametrize
    async def test_raw_response_add_phone_number(self, async_client: AsyncPrelude) -> None:
        response = await async_client.verification_management.sandbox.with_raw_response.add_phone_number(
            attempt_code="123456",
            phone_number="+30123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxAddPhoneNumberResponse, sandbox, path=["response"])

    @parametrize
    async def test_streaming_response_add_phone_number(self, async_client: AsyncPrelude) -> None:
        async with async_client.verification_management.sandbox.with_streaming_response.add_phone_number(
            attempt_code="123456",
            phone_number="+30123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxAddPhoneNumberResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete_phone_number(self, async_client: AsyncPrelude) -> None:
        sandbox = await async_client.verification_management.sandbox.delete_phone_number(
            "+12065550100",
        )
        assert_matches_type(SandboxDeletePhoneNumberResponse, sandbox, path=["response"])

    @parametrize
    async def test_raw_response_delete_phone_number(self, async_client: AsyncPrelude) -> None:
        response = await async_client.verification_management.sandbox.with_raw_response.delete_phone_number(
            "+12065550100",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxDeletePhoneNumberResponse, sandbox, path=["response"])

    @parametrize
    async def test_streaming_response_delete_phone_number(self, async_client: AsyncPrelude) -> None:
        async with async_client.verification_management.sandbox.with_streaming_response.delete_phone_number(
            "+12065550100",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxDeletePhoneNumberResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete_phone_number(self, async_client: AsyncPrelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.verification_management.sandbox.with_raw_response.delete_phone_number(
                "",
            )

    @parametrize
    async def test_method_list_phone_numbers(self, async_client: AsyncPrelude) -> None:
        sandbox = await async_client.verification_management.sandbox.list_phone_numbers()
        assert_matches_type(SandboxListPhoneNumbersResponse, sandbox, path=["response"])

    @parametrize
    async def test_raw_response_list_phone_numbers(self, async_client: AsyncPrelude) -> None:
        response = await async_client.verification_management.sandbox.with_raw_response.list_phone_numbers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxListPhoneNumbersResponse, sandbox, path=["response"])

    @parametrize
    async def test_streaming_response_list_phone_numbers(self, async_client: AsyncPrelude) -> None:
        async with (
            async_client.verification_management.sandbox.with_streaming_response.list_phone_numbers()
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxListPhoneNumbersResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True
