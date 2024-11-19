# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prelude_python_sdk import Prelude, AsyncPrelude
from prelude_python_sdk.types import TransactionalSendResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactional:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_send(self, client: Prelude) -> None:
        transactional = client.transactional.send(
            template_id="template_01jd1xq0cffycayqtdkdbv4d61",
            to="+30123456789",
        )
        assert_matches_type(TransactionalSendResponse, transactional, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_send_with_all_params(self, client: Prelude) -> None:
        transactional = client.transactional.send(
            template_id="template_01jd1xq0cffycayqtdkdbv4d61",
            to="+30123456789",
            callback_url="callback_url",
            correlation_id="correlation_id",
            expires_at="expires_at",
            from_="from",
            variables={"foo": "bar"},
        )
        assert_matches_type(TransactionalSendResponse, transactional, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_raw_response_send(self, client: Prelude) -> None:
        response = client.transactional.with_raw_response.send(
            template_id="template_01jd1xq0cffycayqtdkdbv4d61",
            to="+30123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transactional = response.parse()
        assert_matches_type(TransactionalSendResponse, transactional, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_streaming_response_send(self, client: Prelude) -> None:
        with client.transactional.with_streaming_response.send(
            template_id="template_01jd1xq0cffycayqtdkdbv4d61",
            to="+30123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transactional = response.parse()
            assert_matches_type(TransactionalSendResponse, transactional, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransactional:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_send(self, async_client: AsyncPrelude) -> None:
        transactional = await async_client.transactional.send(
            template_id="template_01jd1xq0cffycayqtdkdbv4d61",
            to="+30123456789",
        )
        assert_matches_type(TransactionalSendResponse, transactional, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncPrelude) -> None:
        transactional = await async_client.transactional.send(
            template_id="template_01jd1xq0cffycayqtdkdbv4d61",
            to="+30123456789",
            callback_url="callback_url",
            correlation_id="correlation_id",
            expires_at="expires_at",
            from_="from",
            variables={"foo": "bar"},
        )
        assert_matches_type(TransactionalSendResponse, transactional, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncPrelude) -> None:
        response = await async_client.transactional.with_raw_response.send(
            template_id="template_01jd1xq0cffycayqtdkdbv4d61",
            to="+30123456789",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transactional = await response.parse()
        assert_matches_type(TransactionalSendResponse, transactional, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncPrelude) -> None:
        async with async_client.transactional.with_streaming_response.send(
            template_id="template_01jd1xq0cffycayqtdkdbv4d61",
            to="+30123456789",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transactional = await response.parse()
            assert_matches_type(TransactionalSendResponse, transactional, path=["response"])

        assert cast(Any, response.is_closed) is True
