# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from prelude_sdk import Prelude, AsyncPrelude
from tests.utils import assert_matches_type
from prelude_sdk.types import (
    VerificationCheckResponse,
    VerificationCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVerification:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Prelude) -> None:
        verification = client.verification.create(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Prelude) -> None:
        verification = client.verification.create(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
            metadata={"correlation_id": "correlation_id"},
            options={
                "locale": "el-GR",
                "sender_id": "sender_id",
                "template_id": "template_id",
            },
            signals={
                "app_realm": "app_realm",
                "app_version": "app_version",
                "device_id": "device_id",
                "device_model": "device_model",
                "device_type": "IOS",
                "ip": "ip",
                "is_trusted_user": "is_trusted_user",
                "os_version": "os_version",
            },
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Prelude) -> None:
        response = client.verification.with_raw_response.create(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Prelude) -> None:
        with client.verification.with_streaming_response.create(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationCreateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_check(self, client: Prelude) -> None:
        verification = client.verification.check(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )
        assert_matches_type(VerificationCheckResponse, verification, path=["response"])

    @parametrize
    def test_method_check_with_all_params(self, client: Prelude) -> None:
        verification = client.verification.check(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
            code="12345",
        )
        assert_matches_type(VerificationCheckResponse, verification, path=["response"])

    @parametrize
    def test_raw_response_check(self, client: Prelude) -> None:
        response = client.verification.with_raw_response.check(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = response.parse()
        assert_matches_type(VerificationCheckResponse, verification, path=["response"])

    @parametrize
    def test_streaming_response_check(self, client: Prelude) -> None:
        with client.verification.with_streaming_response.check(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = response.parse()
            assert_matches_type(VerificationCheckResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVerification:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPrelude) -> None:
        verification = await async_client.verification.create(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPrelude) -> None:
        verification = await async_client.verification.create(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
            metadata={"correlation_id": "correlation_id"},
            options={
                "locale": "el-GR",
                "sender_id": "sender_id",
                "template_id": "template_id",
            },
            signals={
                "app_realm": "app_realm",
                "app_version": "app_version",
                "device_id": "device_id",
                "device_model": "device_model",
                "device_type": "IOS",
                "ip": "ip",
                "is_trusted_user": "is_trusted_user",
                "os_version": "os_version",
            },
        )
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrelude) -> None:
        response = await async_client.verification.with_raw_response.create(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationCreateResponse, verification, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrelude) -> None:
        async with async_client.verification.with_streaming_response.create(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationCreateResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_check(self, async_client: AsyncPrelude) -> None:
        verification = await async_client.verification.check(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )
        assert_matches_type(VerificationCheckResponse, verification, path=["response"])

    @parametrize
    async def test_method_check_with_all_params(self, async_client: AsyncPrelude) -> None:
        verification = await async_client.verification.check(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
            code="12345",
        )
        assert_matches_type(VerificationCheckResponse, verification, path=["response"])

    @parametrize
    async def test_raw_response_check(self, async_client: AsyncPrelude) -> None:
        response = await async_client.verification.with_raw_response.check(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        verification = await response.parse()
        assert_matches_type(VerificationCheckResponse, verification, path=["response"])

    @parametrize
    async def test_streaming_response_check(self, async_client: AsyncPrelude) -> None:
        async with async_client.verification.with_streaming_response.check(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            verification = await response.parse()
            assert_matches_type(VerificationCheckResponse, verification, path=["response"])

        assert cast(Any, response.is_closed) is True
