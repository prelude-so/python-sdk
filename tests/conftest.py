from __future__ import annotations

import os
import logging
from typing import TYPE_CHECKING, Iterator, AsyncIterator

import pytest
from pytest_asyncio import is_async_test

from prelude import Prelude, AsyncPrelude

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest

pytest.register_assert_rewrite("tests.utils")

logging.getLogger("prelude").setLevel(logging.DEBUG)


# automatically add `pytest.mark.asyncio()` to all of our async tests
# so we don't have to add that boilerplate everywhere
def pytest_collection_modifyitems(items: list[pytest.Function]) -> None:
    pytest_asyncio_tests = (item for item in items if is_async_test(item))
    session_scope_marker = pytest.mark.asyncio(loop_scope="session")
    for async_test in pytest_asyncio_tests:
        async_test.add_marker(session_scope_marker, append=False)


base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

api_key = "My API Key"
customer_uuid = "My Customer Uuid"


@pytest.fixture(scope="session")
def client(request: FixtureRequest) -> Iterator[Prelude]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    with Prelude(
        base_url=base_url, api_key=api_key, customer_uuid=customer_uuid, _strict_response_validation=strict
    ) as client:
        yield client


@pytest.fixture(scope="session")
async def async_client(request: FixtureRequest) -> AsyncIterator[AsyncPrelude]:
    strict = getattr(request, "param", True)
    if not isinstance(strict, bool):
        raise TypeError(f"Unexpected fixture parameter type {type(strict)}, expected {bool}")

    async with AsyncPrelude(
        base_url=base_url, api_key=api_key, customer_uuid=customer_uuid, _strict_response_validation=strict
    ) as client:
        yield client