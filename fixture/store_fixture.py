import pytest
from api.store_api.store_api import StoreApi

"""Конектор к StoreApi """


@pytest.fixture(scope="function")
def store_api() -> StoreApi:
    return StoreApi()


@pytest.fixture(scope="function")
def create_place_order_fixture(store_api):
    def _create_place_order_fixture(*args):
        store_api.place_an_order_for_a_pet(*args)

    return _create_place_order_fixture


@pytest.fixture(scope="function")
def delete_place_order_fixture(store_api):
    def _delete_place_order_fixture(*args):
        store_api.delete_order_by_id(*args)

    return _delete_place_order_fixture
