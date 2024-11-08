# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from prelude_sdk import Prelude, AsyncPrelude
from tests.utils import assert_matches_type
from prelude_sdk.types import WatchPredictResponse, WatchFeedbackResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_feedback(self, client: Prelude) -> None:
        watch = client.watch.feedback(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )
        assert_matches_type(WatchFeedbackResponse, watch, path=["response"])

    @parametrize
    def test_method_feedback_with_all_params(self, client: Prelude) -> None:
        watch = client.watch.feedback(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
            feedback={"type": "CONFIRM_PHONE_NUMBER"},
        )
        assert_matches_type(WatchFeedbackResponse, watch, path=["response"])

    @parametrize
    def test_raw_response_feedback(self, client: Prelude) -> None:
        response = client.watch.with_raw_response.feedback(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watch = response.parse()
        assert_matches_type(WatchFeedbackResponse, watch, path=["response"])

    @parametrize
    def test_streaming_response_feedback(self, client: Prelude) -> None:
        with client.watch.with_streaming_response.feedback(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watch = response.parse()
            assert_matches_type(WatchFeedbackResponse, watch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_predict(self, client: Prelude) -> None:
        watch = client.watch.predict(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )
        assert_matches_type(WatchPredictResponse, watch, path=["response"])

    @parametrize
    def test_method_predict_with_all_params(self, client: Prelude) -> None:
        watch = client.watch.predict(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
            signals={
                "device_id": "device_id",
                "device_model": "device_model",
                "device_type": "device_type",
                "ip": "ip",
            },
        )
        assert_matches_type(WatchPredictResponse, watch, path=["response"])

    @parametrize
    def test_raw_response_predict(self, client: Prelude) -> None:
        response = client.watch.with_raw_response.predict(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watch = response.parse()
        assert_matches_type(WatchPredictResponse, watch, path=["response"])

    @parametrize
    def test_streaming_response_predict(self, client: Prelude) -> None:
        with client.watch.with_streaming_response.predict(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watch = response.parse()
            assert_matches_type(WatchPredictResponse, watch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWatch:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_feedback(self, async_client: AsyncPrelude) -> None:
        watch = await async_client.watch.feedback(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )
        assert_matches_type(WatchFeedbackResponse, watch, path=["response"])

    @parametrize
    async def test_method_feedback_with_all_params(self, async_client: AsyncPrelude) -> None:
        watch = await async_client.watch.feedback(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
            feedback={"type": "CONFIRM_PHONE_NUMBER"},
        )
        assert_matches_type(WatchFeedbackResponse, watch, path=["response"])

    @parametrize
    async def test_raw_response_feedback(self, async_client: AsyncPrelude) -> None:
        response = await async_client.watch.with_raw_response.feedback(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watch = await response.parse()
        assert_matches_type(WatchFeedbackResponse, watch, path=["response"])

    @parametrize
    async def test_streaming_response_feedback(self, async_client: AsyncPrelude) -> None:
        async with async_client.watch.with_streaming_response.feedback(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watch = await response.parse()
            assert_matches_type(WatchFeedbackResponse, watch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_predict(self, async_client: AsyncPrelude) -> None:
        watch = await async_client.watch.predict(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )
        assert_matches_type(WatchPredictResponse, watch, path=["response"])

    @parametrize
    async def test_method_predict_with_all_params(self, async_client: AsyncPrelude) -> None:
        watch = await async_client.watch.predict(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
            signals={
                "device_id": "device_id",
                "device_model": "device_model",
                "device_type": "device_type",
                "ip": "ip",
            },
        )
        assert_matches_type(WatchPredictResponse, watch, path=["response"])

    @parametrize
    async def test_raw_response_predict(self, async_client: AsyncPrelude) -> None:
        response = await async_client.watch.with_raw_response.predict(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watch = await response.parse()
        assert_matches_type(WatchPredictResponse, watch, path=["response"])

    @parametrize
    async def test_streaming_response_predict(self, async_client: AsyncPrelude) -> None:
        async with async_client.watch.with_streaming_response.predict(
            target={
                "type": "phone_number",
                "value": "+30123456789",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watch = await response.parse()
            assert_matches_type(WatchPredictResponse, watch, path=["response"])

        assert cast(Any, response.is_closed) is True