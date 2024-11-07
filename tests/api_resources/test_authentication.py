# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from prelude import Prelude, AsyncPrelude
from tests.utils import assert_matches_type
from prelude.types import AuthenticationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthentication:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Prelude) -> None:
        authentication = client.authentication.create(
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_number="+1234567890",
        )
        assert_matches_type(AuthenticationCreateResponse, authentication, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Prelude) -> None:
        authentication = client.authentication.create(
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_number="+1234567890",
            app_realm="app_realm",
            app_version="app_version",
            callback_url="callback_url",
            device_id="device_id",
            device_model="device_model",
            device_type="IOS",
            ip="ip",
            is_returning_user=True,
            os_version="os_version",
            template_id="template_id",
        )
        assert_matches_type(AuthenticationCreateResponse, authentication, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Prelude) -> None:
        response = client.authentication.with_raw_response.create(
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_number="+1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationCreateResponse, authentication, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Prelude) -> None:
        with client.authentication.with_streaming_response.create(
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_number="+1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert_matches_type(AuthenticationCreateResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuthentication:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPrelude) -> None:
        authentication = await async_client.authentication.create(
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_number="+1234567890",
        )
        assert_matches_type(AuthenticationCreateResponse, authentication, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPrelude) -> None:
        authentication = await async_client.authentication.create(
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_number="+1234567890",
            app_realm="app_realm",
            app_version="app_version",
            callback_url="callback_url",
            device_id="device_id",
            device_model="device_model",
            device_type="IOS",
            ip="ip",
            is_returning_user=True,
            os_version="os_version",
            template_id="template_id",
        )
        assert_matches_type(AuthenticationCreateResponse, authentication, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPrelude) -> None:
        response = await async_client.authentication.with_raw_response.create(
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_number="+1234567890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = await response.parse()
        assert_matches_type(AuthenticationCreateResponse, authentication, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPrelude) -> None:
        async with async_client.authentication.with_streaming_response.create(
            customer_uuid="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            phone_number="+1234567890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert_matches_type(AuthenticationCreateResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True
