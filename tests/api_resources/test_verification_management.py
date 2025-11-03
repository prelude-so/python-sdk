# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prelude_python_sdk import Prelude, AsyncPrelude
from prelude_python_sdk.types import (
    VerificationManagementListSenderIDsResponse,
    VerificationManagementSetPhoneNumberResponse,
    VerificationManagementSubmitSenderIDResponse,
    VerificationManagementListPhoneNumbersResponse,
    VerificationManagementDeletePhoneNumberResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerificationManagement:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete_phone_number(self, client: Prelude) -> None:
        verification_management = client.verification_management.delete_phone_number(
            action="allow",
            phone_number="+30123456789",
        )
        assert_matches_type(VerificationManagementDeletePhoneNumberResponse, verification_management, path=["response"])

    @parametrize
    def test_raw_response_delete_phone_number(self, client: Prelude) -> None:
        response = client.verification_management.with_raw_response.delete_phone_number(
            action="allow",
            phone_number="+30123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_management = response.parse()
        assert_matches_type(VerificationManagementDeletePhoneNumberResponse, verification_management, path=["response"])

    @parametrize
    def test_streaming_response_delete_phone_number(self, client: Prelude) -> None:
        with client.verification_management.with_streaming_response.delete_phone_number(
            action="allow",
            phone_number="+30123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_management = response.parse()
            assert_matches_type(
                VerificationManagementDeletePhoneNumberResponse, verification_management, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_phone_numbers(self, client: Prelude) -> None:
        verification_management = client.verification_management.list_phone_numbers(
            "allow",
        )
        assert_matches_type(VerificationManagementListPhoneNumbersResponse, verification_management, path=["response"])

    @parametrize
    def test_raw_response_list_phone_numbers(self, client: Prelude) -> None:
        response = client.verification_management.with_raw_response.list_phone_numbers(
            "allow",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_management = response.parse()
        assert_matches_type(VerificationManagementListPhoneNumbersResponse, verification_management, path=["response"])

    @parametrize
    def test_streaming_response_list_phone_numbers(self, client: Prelude) -> None:
        with client.verification_management.with_streaming_response.list_phone_numbers(
            "allow",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_management = response.parse()
            assert_matches_type(
                VerificationManagementListPhoneNumbersResponse, verification_management, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_sender_ids(self, client: Prelude) -> None:
        verification_management = client.verification_management.list_sender_ids()
        assert_matches_type(VerificationManagementListSenderIDsResponse, verification_management, path=["response"])

    @parametrize
    def test_raw_response_list_sender_ids(self, client: Prelude) -> None:
        response = client.verification_management.with_raw_response.list_sender_ids()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_management = response.parse()
        assert_matches_type(VerificationManagementListSenderIDsResponse, verification_management, path=["response"])

    @parametrize
    def test_streaming_response_list_sender_ids(self, client: Prelude) -> None:
        with client.verification_management.with_streaming_response.list_sender_ids() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_management = response.parse()
            assert_matches_type(VerificationManagementListSenderIDsResponse, verification_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_set_phone_number(self, client: Prelude) -> None:
        verification_management = client.verification_management.set_phone_number(
            action="allow",
            phone_number="+30123456789",
        )
        assert_matches_type(VerificationManagementSetPhoneNumberResponse, verification_management, path=["response"])

    @parametrize
    def test_raw_response_set_phone_number(self, client: Prelude) -> None:
        response = client.verification_management.with_raw_response.set_phone_number(
            action="allow",
            phone_number="+30123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_management = response.parse()
        assert_matches_type(VerificationManagementSetPhoneNumberResponse, verification_management, path=["response"])

    @parametrize
    def test_streaming_response_set_phone_number(self, client: Prelude) -> None:
        with client.verification_management.with_streaming_response.set_phone_number(
            action="allow",
            phone_number="+30123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_management = response.parse()
            assert_matches_type(
                VerificationManagementSetPhoneNumberResponse, verification_management, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_submit_sender_id(self, client: Prelude) -> None:
        verification_management = client.verification_management.submit_sender_id(
            sender_id="Prelude",
        )
        assert_matches_type(VerificationManagementSubmitSenderIDResponse, verification_management, path=["response"])

    @parametrize
    def test_raw_response_submit_sender_id(self, client: Prelude) -> None:
        response = client.verification_management.with_raw_response.submit_sender_id(
            sender_id="Prelude",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_management = response.parse()
        assert_matches_type(VerificationManagementSubmitSenderIDResponse, verification_management, path=["response"])

    @parametrize
    def test_streaming_response_submit_sender_id(self, client: Prelude) -> None:
        with client.verification_management.with_streaming_response.submit_sender_id(
            sender_id="Prelude",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_management = response.parse()
            assert_matches_type(
                VerificationManagementSubmitSenderIDResponse, verification_management, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncVerificationManagement:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete_phone_number(self, async_client: AsyncPrelude) -> None:
        verification_management = await async_client.verification_management.delete_phone_number(
            action="allow",
            phone_number="+30123456789",
        )
        assert_matches_type(VerificationManagementDeletePhoneNumberResponse, verification_management, path=["response"])

    @parametrize
    async def test_raw_response_delete_phone_number(self, async_client: AsyncPrelude) -> None:
        response = await async_client.verification_management.with_raw_response.delete_phone_number(
            action="allow",
            phone_number="+30123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_management = await response.parse()
        assert_matches_type(VerificationManagementDeletePhoneNumberResponse, verification_management, path=["response"])

    @parametrize
    async def test_streaming_response_delete_phone_number(self, async_client: AsyncPrelude) -> None:
        async with async_client.verification_management.with_streaming_response.delete_phone_number(
            action="allow",
            phone_number="+30123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_management = await response.parse()
            assert_matches_type(
                VerificationManagementDeletePhoneNumberResponse, verification_management, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_phone_numbers(self, async_client: AsyncPrelude) -> None:
        verification_management = await async_client.verification_management.list_phone_numbers(
            "allow",
        )
        assert_matches_type(VerificationManagementListPhoneNumbersResponse, verification_management, path=["response"])

    @parametrize
    async def test_raw_response_list_phone_numbers(self, async_client: AsyncPrelude) -> None:
        response = await async_client.verification_management.with_raw_response.list_phone_numbers(
            "allow",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_management = await response.parse()
        assert_matches_type(VerificationManagementListPhoneNumbersResponse, verification_management, path=["response"])

    @parametrize
    async def test_streaming_response_list_phone_numbers(self, async_client: AsyncPrelude) -> None:
        async with async_client.verification_management.with_streaming_response.list_phone_numbers(
            "allow",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_management = await response.parse()
            assert_matches_type(
                VerificationManagementListPhoneNumbersResponse, verification_management, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_sender_ids(self, async_client: AsyncPrelude) -> None:
        verification_management = await async_client.verification_management.list_sender_ids()
        assert_matches_type(VerificationManagementListSenderIDsResponse, verification_management, path=["response"])

    @parametrize
    async def test_raw_response_list_sender_ids(self, async_client: AsyncPrelude) -> None:
        response = await async_client.verification_management.with_raw_response.list_sender_ids()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_management = await response.parse()
        assert_matches_type(VerificationManagementListSenderIDsResponse, verification_management, path=["response"])

    @parametrize
    async def test_streaming_response_list_sender_ids(self, async_client: AsyncPrelude) -> None:
        async with async_client.verification_management.with_streaming_response.list_sender_ids() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_management = await response.parse()
            assert_matches_type(VerificationManagementListSenderIDsResponse, verification_management, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_set_phone_number(self, async_client: AsyncPrelude) -> None:
        verification_management = await async_client.verification_management.set_phone_number(
            action="allow",
            phone_number="+30123456789",
        )
        assert_matches_type(VerificationManagementSetPhoneNumberResponse, verification_management, path=["response"])

    @parametrize
    async def test_raw_response_set_phone_number(self, async_client: AsyncPrelude) -> None:
        response = await async_client.verification_management.with_raw_response.set_phone_number(
            action="allow",
            phone_number="+30123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_management = await response.parse()
        assert_matches_type(VerificationManagementSetPhoneNumberResponse, verification_management, path=["response"])

    @parametrize
    async def test_streaming_response_set_phone_number(self, async_client: AsyncPrelude) -> None:
        async with async_client.verification_management.with_streaming_response.set_phone_number(
            action="allow",
            phone_number="+30123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_management = await response.parse()
            assert_matches_type(
                VerificationManagementSetPhoneNumberResponse, verification_management, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_submit_sender_id(self, async_client: AsyncPrelude) -> None:
        verification_management = await async_client.verification_management.submit_sender_id(
            sender_id="Prelude",
        )
        assert_matches_type(VerificationManagementSubmitSenderIDResponse, verification_management, path=["response"])

    @parametrize
    async def test_raw_response_submit_sender_id(self, async_client: AsyncPrelude) -> None:
        response = await async_client.verification_management.with_raw_response.submit_sender_id(
            sender_id="Prelude",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification_management = await response.parse()
        assert_matches_type(VerificationManagementSubmitSenderIDResponse, verification_management, path=["response"])

    @parametrize
    async def test_streaming_response_submit_sender_id(self, async_client: AsyncPrelude) -> None:
        async with async_client.verification_management.with_streaming_response.submit_sender_id(
            sender_id="Prelude",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification_management = await response.parse()
            assert_matches_type(
                VerificationManagementSubmitSenderIDResponse, verification_management, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
