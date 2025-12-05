# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prelude_python_sdk import Prelude, AsyncPrelude
from prelude_python_sdk.types import (
    NotifySendResponse,
    NotifySendBatchResponse,
    NotifyGetSubscriptionConfigResponse,
    NotifyListSubscriptionConfigsResponse,
    NotifyGetSubscriptionPhoneNumberResponse,
    NotifyListSubscriptionPhoneNumbersResponse,
    NotifyListSubscriptionPhoneNumberEventsResponse,
)
from prelude_python_sdk._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNotify:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_subscription_config(self, client: Prelude) -> None:
        notify = client.notify.get_subscription_config(
            "config_id",
        )
        assert_matches_type(NotifyGetSubscriptionConfigResponse, notify, path=["response"])

    @parametrize
    def test_raw_response_get_subscription_config(self, client: Prelude) -> None:
        response = client.notify.with_raw_response.get_subscription_config(
            "config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notify = response.parse()
        assert_matches_type(NotifyGetSubscriptionConfigResponse, notify, path=["response"])

    @parametrize
    def test_streaming_response_get_subscription_config(self, client: Prelude) -> None:
        with client.notify.with_streaming_response.get_subscription_config(
            "config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notify = response.parse()
            assert_matches_type(NotifyGetSubscriptionConfigResponse, notify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_subscription_config(self, client: Prelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.notify.with_raw_response.get_subscription_config(
                "",
            )

    @parametrize
    def test_method_get_subscription_phone_number(self, client: Prelude) -> None:
        notify = client.notify.get_subscription_phone_number(
            phone_number="phone_number",
            config_id="config_id",
        )
        assert_matches_type(NotifyGetSubscriptionPhoneNumberResponse, notify, path=["response"])

    @parametrize
    def test_raw_response_get_subscription_phone_number(self, client: Prelude) -> None:
        response = client.notify.with_raw_response.get_subscription_phone_number(
            phone_number="phone_number",
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notify = response.parse()
        assert_matches_type(NotifyGetSubscriptionPhoneNumberResponse, notify, path=["response"])

    @parametrize
    def test_streaming_response_get_subscription_phone_number(self, client: Prelude) -> None:
        with client.notify.with_streaming_response.get_subscription_phone_number(
            phone_number="phone_number",
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notify = response.parse()
            assert_matches_type(NotifyGetSubscriptionPhoneNumberResponse, notify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_subscription_phone_number(self, client: Prelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.notify.with_raw_response.get_subscription_phone_number(
                phone_number="phone_number",
                config_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.notify.with_raw_response.get_subscription_phone_number(
                phone_number="",
                config_id="config_id",
            )

    @parametrize
    def test_method_list_subscription_configs(self, client: Prelude) -> None:
        notify = client.notify.list_subscription_configs()
        assert_matches_type(NotifyListSubscriptionConfigsResponse, notify, path=["response"])

    @parametrize
    def test_method_list_subscription_configs_with_all_params(self, client: Prelude) -> None:
        notify = client.notify.list_subscription_configs(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(NotifyListSubscriptionConfigsResponse, notify, path=["response"])

    @parametrize
    def test_raw_response_list_subscription_configs(self, client: Prelude) -> None:
        response = client.notify.with_raw_response.list_subscription_configs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notify = response.parse()
        assert_matches_type(NotifyListSubscriptionConfigsResponse, notify, path=["response"])

    @parametrize
    def test_streaming_response_list_subscription_configs(self, client: Prelude) -> None:
        with client.notify.with_streaming_response.list_subscription_configs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notify = response.parse()
            assert_matches_type(NotifyListSubscriptionConfigsResponse, notify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_subscription_phone_number_events(self, client: Prelude) -> None:
        notify = client.notify.list_subscription_phone_number_events(
            phone_number="phone_number",
            config_id="config_id",
        )
        assert_matches_type(NotifyListSubscriptionPhoneNumberEventsResponse, notify, path=["response"])

    @parametrize
    def test_method_list_subscription_phone_number_events_with_all_params(self, client: Prelude) -> None:
        notify = client.notify.list_subscription_phone_number_events(
            phone_number="phone_number",
            config_id="config_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(NotifyListSubscriptionPhoneNumberEventsResponse, notify, path=["response"])

    @parametrize
    def test_raw_response_list_subscription_phone_number_events(self, client: Prelude) -> None:
        response = client.notify.with_raw_response.list_subscription_phone_number_events(
            phone_number="phone_number",
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notify = response.parse()
        assert_matches_type(NotifyListSubscriptionPhoneNumberEventsResponse, notify, path=["response"])

    @parametrize
    def test_streaming_response_list_subscription_phone_number_events(self, client: Prelude) -> None:
        with client.notify.with_streaming_response.list_subscription_phone_number_events(
            phone_number="phone_number",
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notify = response.parse()
            assert_matches_type(NotifyListSubscriptionPhoneNumberEventsResponse, notify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_subscription_phone_number_events(self, client: Prelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.notify.with_raw_response.list_subscription_phone_number_events(
                phone_number="phone_number",
                config_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            client.notify.with_raw_response.list_subscription_phone_number_events(
                phone_number="",
                config_id="config_id",
            )

    @parametrize
    def test_method_list_subscription_phone_numbers(self, client: Prelude) -> None:
        notify = client.notify.list_subscription_phone_numbers(
            config_id="config_id",
        )
        assert_matches_type(NotifyListSubscriptionPhoneNumbersResponse, notify, path=["response"])

    @parametrize
    def test_method_list_subscription_phone_numbers_with_all_params(self, client: Prelude) -> None:
        notify = client.notify.list_subscription_phone_numbers(
            config_id="config_id",
            cursor="cursor",
            limit=1,
            state="SUB",
        )
        assert_matches_type(NotifyListSubscriptionPhoneNumbersResponse, notify, path=["response"])

    @parametrize
    def test_raw_response_list_subscription_phone_numbers(self, client: Prelude) -> None:
        response = client.notify.with_raw_response.list_subscription_phone_numbers(
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notify = response.parse()
        assert_matches_type(NotifyListSubscriptionPhoneNumbersResponse, notify, path=["response"])

    @parametrize
    def test_streaming_response_list_subscription_phone_numbers(self, client: Prelude) -> None:
        with client.notify.with_streaming_response.list_subscription_phone_numbers(
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notify = response.parse()
            assert_matches_type(NotifyListSubscriptionPhoneNumbersResponse, notify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list_subscription_phone_numbers(self, client: Prelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.notify.with_raw_response.list_subscription_phone_numbers(
                config_id="",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_send(self, client: Prelude) -> None:
        notify = client.notify.send(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to="+33612345678",
        )
        assert_matches_type(NotifySendResponse, notify, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_method_send_with_all_params(self, client: Prelude) -> None:
        notify = client.notify.send(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to="+33612345678",
            callback_url="https://your-app.com/webhooks/notify",
            correlation_id="order-12345",
            expires_at=parse_datetime("2025-12-25T18:00:00Z"),
            from_="from",
            locale="el-GR",
            preferred_channel="whatsapp",
            schedule_at=parse_datetime("2025-12-25T10:00:00Z"),
            variables={
                "order_id": "12345",
                "amount": "$49.99",
            },
        )
        assert_matches_type(NotifySendResponse, notify, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_raw_response_send(self, client: Prelude) -> None:
        response = client.notify.with_raw_response.send(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to="+33612345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notify = response.parse()
        assert_matches_type(NotifySendResponse, notify, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    def test_streaming_response_send(self, client: Prelude) -> None:
        with client.notify.with_streaming_response.send(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to="+33612345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notify = response.parse()
            assert_matches_type(NotifySendResponse, notify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_send_batch(self, client: Prelude) -> None:
        notify = client.notify.send_batch(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to=["+33612345678", "+15551234567"],
        )
        assert_matches_type(NotifySendBatchResponse, notify, path=["response"])

    @parametrize
    def test_method_send_batch_with_all_params(self, client: Prelude) -> None:
        notify = client.notify.send_batch(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to=["+33612345678", "+15551234567"],
            callback_url="https://your-app.com/webhooks/notify",
            correlation_id="campaign-12345",
            expires_at=parse_datetime("2025-12-25T18:00:00Z"),
            from_="from",
            locale="el-GR",
            preferred_channel="whatsapp",
            schedule_at=parse_datetime("2025-12-25T10:00:00Z"),
            variables={
                "order_id": "12345",
                "amount": "$49.99",
            },
        )
        assert_matches_type(NotifySendBatchResponse, notify, path=["response"])

    @parametrize
    def test_raw_response_send_batch(self, client: Prelude) -> None:
        response = client.notify.with_raw_response.send_batch(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to=["+33612345678", "+15551234567"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notify = response.parse()
        assert_matches_type(NotifySendBatchResponse, notify, path=["response"])

    @parametrize
    def test_streaming_response_send_batch(self, client: Prelude) -> None:
        with client.notify.with_streaming_response.send_batch(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to=["+33612345678", "+15551234567"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notify = response.parse()
            assert_matches_type(NotifySendBatchResponse, notify, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNotify:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_subscription_config(self, async_client: AsyncPrelude) -> None:
        notify = await async_client.notify.get_subscription_config(
            "config_id",
        )
        assert_matches_type(NotifyGetSubscriptionConfigResponse, notify, path=["response"])

    @parametrize
    async def test_raw_response_get_subscription_config(self, async_client: AsyncPrelude) -> None:
        response = await async_client.notify.with_raw_response.get_subscription_config(
            "config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notify = await response.parse()
        assert_matches_type(NotifyGetSubscriptionConfigResponse, notify, path=["response"])

    @parametrize
    async def test_streaming_response_get_subscription_config(self, async_client: AsyncPrelude) -> None:
        async with async_client.notify.with_streaming_response.get_subscription_config(
            "config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notify = await response.parse()
            assert_matches_type(NotifyGetSubscriptionConfigResponse, notify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_subscription_config(self, async_client: AsyncPrelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.notify.with_raw_response.get_subscription_config(
                "",
            )

    @parametrize
    async def test_method_get_subscription_phone_number(self, async_client: AsyncPrelude) -> None:
        notify = await async_client.notify.get_subscription_phone_number(
            phone_number="phone_number",
            config_id="config_id",
        )
        assert_matches_type(NotifyGetSubscriptionPhoneNumberResponse, notify, path=["response"])

    @parametrize
    async def test_raw_response_get_subscription_phone_number(self, async_client: AsyncPrelude) -> None:
        response = await async_client.notify.with_raw_response.get_subscription_phone_number(
            phone_number="phone_number",
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notify = await response.parse()
        assert_matches_type(NotifyGetSubscriptionPhoneNumberResponse, notify, path=["response"])

    @parametrize
    async def test_streaming_response_get_subscription_phone_number(self, async_client: AsyncPrelude) -> None:
        async with async_client.notify.with_streaming_response.get_subscription_phone_number(
            phone_number="phone_number",
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notify = await response.parse()
            assert_matches_type(NotifyGetSubscriptionPhoneNumberResponse, notify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_subscription_phone_number(self, async_client: AsyncPrelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.notify.with_raw_response.get_subscription_phone_number(
                phone_number="phone_number",
                config_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.notify.with_raw_response.get_subscription_phone_number(
                phone_number="",
                config_id="config_id",
            )

    @parametrize
    async def test_method_list_subscription_configs(self, async_client: AsyncPrelude) -> None:
        notify = await async_client.notify.list_subscription_configs()
        assert_matches_type(NotifyListSubscriptionConfigsResponse, notify, path=["response"])

    @parametrize
    async def test_method_list_subscription_configs_with_all_params(self, async_client: AsyncPrelude) -> None:
        notify = await async_client.notify.list_subscription_configs(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(NotifyListSubscriptionConfigsResponse, notify, path=["response"])

    @parametrize
    async def test_raw_response_list_subscription_configs(self, async_client: AsyncPrelude) -> None:
        response = await async_client.notify.with_raw_response.list_subscription_configs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notify = await response.parse()
        assert_matches_type(NotifyListSubscriptionConfigsResponse, notify, path=["response"])

    @parametrize
    async def test_streaming_response_list_subscription_configs(self, async_client: AsyncPrelude) -> None:
        async with async_client.notify.with_streaming_response.list_subscription_configs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notify = await response.parse()
            assert_matches_type(NotifyListSubscriptionConfigsResponse, notify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_subscription_phone_number_events(self, async_client: AsyncPrelude) -> None:
        notify = await async_client.notify.list_subscription_phone_number_events(
            phone_number="phone_number",
            config_id="config_id",
        )
        assert_matches_type(NotifyListSubscriptionPhoneNumberEventsResponse, notify, path=["response"])

    @parametrize
    async def test_method_list_subscription_phone_number_events_with_all_params(
        self, async_client: AsyncPrelude
    ) -> None:
        notify = await async_client.notify.list_subscription_phone_number_events(
            phone_number="phone_number",
            config_id="config_id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(NotifyListSubscriptionPhoneNumberEventsResponse, notify, path=["response"])

    @parametrize
    async def test_raw_response_list_subscription_phone_number_events(self, async_client: AsyncPrelude) -> None:
        response = await async_client.notify.with_raw_response.list_subscription_phone_number_events(
            phone_number="phone_number",
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notify = await response.parse()
        assert_matches_type(NotifyListSubscriptionPhoneNumberEventsResponse, notify, path=["response"])

    @parametrize
    async def test_streaming_response_list_subscription_phone_number_events(self, async_client: AsyncPrelude) -> None:
        async with async_client.notify.with_streaming_response.list_subscription_phone_number_events(
            phone_number="phone_number",
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notify = await response.parse()
            assert_matches_type(NotifyListSubscriptionPhoneNumberEventsResponse, notify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_subscription_phone_number_events(self, async_client: AsyncPrelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.notify.with_raw_response.list_subscription_phone_number_events(
                phone_number="phone_number",
                config_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `phone_number` but received ''"):
            await async_client.notify.with_raw_response.list_subscription_phone_number_events(
                phone_number="",
                config_id="config_id",
            )

    @parametrize
    async def test_method_list_subscription_phone_numbers(self, async_client: AsyncPrelude) -> None:
        notify = await async_client.notify.list_subscription_phone_numbers(
            config_id="config_id",
        )
        assert_matches_type(NotifyListSubscriptionPhoneNumbersResponse, notify, path=["response"])

    @parametrize
    async def test_method_list_subscription_phone_numbers_with_all_params(self, async_client: AsyncPrelude) -> None:
        notify = await async_client.notify.list_subscription_phone_numbers(
            config_id="config_id",
            cursor="cursor",
            limit=1,
            state="SUB",
        )
        assert_matches_type(NotifyListSubscriptionPhoneNumbersResponse, notify, path=["response"])

    @parametrize
    async def test_raw_response_list_subscription_phone_numbers(self, async_client: AsyncPrelude) -> None:
        response = await async_client.notify.with_raw_response.list_subscription_phone_numbers(
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notify = await response.parse()
        assert_matches_type(NotifyListSubscriptionPhoneNumbersResponse, notify, path=["response"])

    @parametrize
    async def test_streaming_response_list_subscription_phone_numbers(self, async_client: AsyncPrelude) -> None:
        async with async_client.notify.with_streaming_response.list_subscription_phone_numbers(
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notify = await response.parse()
            assert_matches_type(NotifyListSubscriptionPhoneNumbersResponse, notify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list_subscription_phone_numbers(self, async_client: AsyncPrelude) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.notify.with_raw_response.list_subscription_phone_numbers(
                config_id="",
            )

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_send(self, async_client: AsyncPrelude) -> None:
        notify = await async_client.notify.send(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to="+33612345678",
        )
        assert_matches_type(NotifySendResponse, notify, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncPrelude) -> None:
        notify = await async_client.notify.send(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to="+33612345678",
            callback_url="https://your-app.com/webhooks/notify",
            correlation_id="order-12345",
            expires_at=parse_datetime("2025-12-25T18:00:00Z"),
            from_="from",
            locale="el-GR",
            preferred_channel="whatsapp",
            schedule_at=parse_datetime("2025-12-25T10:00:00Z"),
            variables={
                "order_id": "12345",
                "amount": "$49.99",
            },
        )
        assert_matches_type(NotifySendResponse, notify, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncPrelude) -> None:
        response = await async_client.notify.with_raw_response.send(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to="+33612345678",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notify = await response.parse()
        assert_matches_type(NotifySendResponse, notify, path=["response"])

    @pytest.mark.skip(reason="Prism doesn't support callbacks yet")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncPrelude) -> None:
        async with async_client.notify.with_streaming_response.send(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to="+33612345678",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notify = await response.parse()
            assert_matches_type(NotifySendResponse, notify, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_send_batch(self, async_client: AsyncPrelude) -> None:
        notify = await async_client.notify.send_batch(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to=["+33612345678", "+15551234567"],
        )
        assert_matches_type(NotifySendBatchResponse, notify, path=["response"])

    @parametrize
    async def test_method_send_batch_with_all_params(self, async_client: AsyncPrelude) -> None:
        notify = await async_client.notify.send_batch(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to=["+33612345678", "+15551234567"],
            callback_url="https://your-app.com/webhooks/notify",
            correlation_id="campaign-12345",
            expires_at=parse_datetime("2025-12-25T18:00:00Z"),
            from_="from",
            locale="el-GR",
            preferred_channel="whatsapp",
            schedule_at=parse_datetime("2025-12-25T10:00:00Z"),
            variables={
                "order_id": "12345",
                "amount": "$49.99",
            },
        )
        assert_matches_type(NotifySendBatchResponse, notify, path=["response"])

    @parametrize
    async def test_raw_response_send_batch(self, async_client: AsyncPrelude) -> None:
        response = await async_client.notify.with_raw_response.send_batch(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to=["+33612345678", "+15551234567"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        notify = await response.parse()
        assert_matches_type(NotifySendBatchResponse, notify, path=["response"])

    @parametrize
    async def test_streaming_response_send_batch(self, async_client: AsyncPrelude) -> None:
        async with async_client.notify.with_streaming_response.send_batch(
            template_id="template_01k8ap1btqf5r9fq2c8ax5fhc9",
            to=["+33612345678", "+15551234567"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            notify = await response.parse()
            assert_matches_type(NotifySendBatchResponse, notify, path=["response"])

        assert cast(Any, response.is_closed) is True
