# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prelude_python_sdk import Prelude, AsyncPrelude
from prelude_python_sdk.types import (
    WatchPredictResponse,
    WatchSendEventsResponse,
    WatchSendFeedbacksResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

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
            dispatch_id="dispatch_id",
            metadata={"correlation_id": "correlation_id"},
            signals={
                "app_version": "1.2.34",
                "device_id": "8F0B8FDD-C2CB-4387-B20A-56E9B2E5A0D2",
                "device_model": "iPhone17,2",
                "device_platform": "ios",
                "ip": "192.0.2.1",
                "is_trusted_user": False,
                "os_version": "18.0.1",
                "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
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

    @parametrize
    def test_method_send_events(self, client: Prelude) -> None:
        watch = client.watch.send_events(
            events=[
                {
                    "confidence": "maximum",
                    "label": "onboarding.start",
                    "target": {
                        "type": "phone_number",
                        "value": "+30123456789",
                    },
                }
            ],
        )
        assert_matches_type(WatchSendEventsResponse, watch, path=["response"])

    @parametrize
    def test_raw_response_send_events(self, client: Prelude) -> None:
        response = client.watch.with_raw_response.send_events(
            events=[
                {
                    "confidence": "maximum",
                    "label": "onboarding.start",
                    "target": {
                        "type": "phone_number",
                        "value": "+30123456789",
                    },
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watch = response.parse()
        assert_matches_type(WatchSendEventsResponse, watch, path=["response"])

    @parametrize
    def test_streaming_response_send_events(self, client: Prelude) -> None:
        with client.watch.with_streaming_response.send_events(
            events=[
                {
                    "confidence": "maximum",
                    "label": "onboarding.start",
                    "target": {
                        "type": "phone_number",
                        "value": "+30123456789",
                    },
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watch = response.parse()
            assert_matches_type(WatchSendEventsResponse, watch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_feedbacks(self, client: Prelude) -> None:
        watch = client.watch.send_feedbacks(
            feedbacks=[
                {
                    "target": {
                        "type": "phone_number",
                        "value": "+30123456789",
                    },
                    "type": "verification.started",
                }
            ],
        )
        assert_matches_type(WatchSendFeedbacksResponse, watch, path=["response"])

    @parametrize
    def test_raw_response_send_feedbacks(self, client: Prelude) -> None:
        response = client.watch.with_raw_response.send_feedbacks(
            feedbacks=[
                {
                    "target": {
                        "type": "phone_number",
                        "value": "+30123456789",
                    },
                    "type": "verification.started",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watch = response.parse()
        assert_matches_type(WatchSendFeedbacksResponse, watch, path=["response"])

    @parametrize
    def test_streaming_response_send_feedbacks(self, client: Prelude) -> None:
        with client.watch.with_streaming_response.send_feedbacks(
            feedbacks=[
                {
                    "target": {
                        "type": "phone_number",
                        "value": "+30123456789",
                    },
                    "type": "verification.started",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watch = response.parse()
            assert_matches_type(WatchSendFeedbacksResponse, watch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWatch:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

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
            dispatch_id="dispatch_id",
            metadata={"correlation_id": "correlation_id"},
            signals={
                "app_version": "1.2.34",
                "device_id": "8F0B8FDD-C2CB-4387-B20A-56E9B2E5A0D2",
                "device_model": "iPhone17,2",
                "device_platform": "ios",
                "ip": "192.0.2.1",
                "is_trusted_user": False,
                "os_version": "18.0.1",
                "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
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

    @parametrize
    async def test_method_send_events(self, async_client: AsyncPrelude) -> None:
        watch = await async_client.watch.send_events(
            events=[
                {
                    "confidence": "maximum",
                    "label": "onboarding.start",
                    "target": {
                        "type": "phone_number",
                        "value": "+30123456789",
                    },
                }
            ],
        )
        assert_matches_type(WatchSendEventsResponse, watch, path=["response"])

    @parametrize
    async def test_raw_response_send_events(self, async_client: AsyncPrelude) -> None:
        response = await async_client.watch.with_raw_response.send_events(
            events=[
                {
                    "confidence": "maximum",
                    "label": "onboarding.start",
                    "target": {
                        "type": "phone_number",
                        "value": "+30123456789",
                    },
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watch = await response.parse()
        assert_matches_type(WatchSendEventsResponse, watch, path=["response"])

    @parametrize
    async def test_streaming_response_send_events(self, async_client: AsyncPrelude) -> None:
        async with async_client.watch.with_streaming_response.send_events(
            events=[
                {
                    "confidence": "maximum",
                    "label": "onboarding.start",
                    "target": {
                        "type": "phone_number",
                        "value": "+30123456789",
                    },
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watch = await response.parse()
            assert_matches_type(WatchSendEventsResponse, watch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_feedbacks(self, async_client: AsyncPrelude) -> None:
        watch = await async_client.watch.send_feedbacks(
            feedbacks=[
                {
                    "target": {
                        "type": "phone_number",
                        "value": "+30123456789",
                    },
                    "type": "verification.started",
                }
            ],
        )
        assert_matches_type(WatchSendFeedbacksResponse, watch, path=["response"])

    @parametrize
    async def test_raw_response_send_feedbacks(self, async_client: AsyncPrelude) -> None:
        response = await async_client.watch.with_raw_response.send_feedbacks(
            feedbacks=[
                {
                    "target": {
                        "type": "phone_number",
                        "value": "+30123456789",
                    },
                    "type": "verification.started",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watch = await response.parse()
        assert_matches_type(WatchSendFeedbacksResponse, watch, path=["response"])

    @parametrize
    async def test_streaming_response_send_feedbacks(self, async_client: AsyncPrelude) -> None:
        async with async_client.watch.with_streaming_response.send_feedbacks(
            feedbacks=[
                {
                    "target": {
                        "type": "phone_number",
                        "value": "+30123456789",
                    },
                    "type": "verification.started",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watch = await response.parse()
            assert_matches_type(WatchSendFeedbacksResponse, watch, path=["response"])

        assert cast(Any, response.is_closed) is True
