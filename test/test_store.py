import pytest
import allure
from data.store_data.store_data import (create_order_valid, create_order_no_valid, response_create_order_valid,
                                        response_create_order_no_valid, response_find_valid, response_find_no_valid,
                                        response_delete_valid, response_delete_no_valid)
from schemas.store_schemas import STORE_SCHEMA, ERROR_DELETE_STORE_SCHEMA
from fixture.store_fixture import create_place_order_fixture, delete_place_order_fixture

pytest_plugins = ["fixture.store_fixture"]


@allure.feature("store_test")
@pytest.mark.parametrize("create_order_val", [create_order_valid])
def test_place_order_for_store_valid(store_api, create_order_val, delete_place_order_fixture):
    store_api.place_an_order_for_a_pet(create_order_val)
    store_api.status_code_should_be(500)
    store_api.assert_schema_is_valid(STORE_SCHEMA)
    store_api.assert_objects_is_equal(response_create_order_valid, store_api.json_representation_store())
    delete_place_order_fixture(create_order_val.id)


@allure.feature("store_test")
@pytest.mark.parametrize("create_order_no_val", [create_order_no_valid])
def test_place_order_for_store_no_valid(store_api, create_order_no_val):
    store_api.place_an_order_for_a_pet(create_order_no_val)
    store_api.status_code_should_be(500)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)
    store_api.assert_objects_is_equal(response_create_order_no_valid, store_api.json_representation())


@allure.feature("store_test")
@pytest.mark.parametrize("create_order_val", [create_order_valid])
def test_find_order_by_id_valid(store_api, create_place_order_fixture, create_order_val,
                                delete_place_order_fixture):
    create_place_order_fixture(create_order_val)
    store_api.find_order_by_id(create_order_val.id)
    store_api.status_code_should_be(200)
    store_api.assert_schema_is_valid(STORE_SCHEMA)
    store_api.assert_objects_is_equal(response_find_valid, store_api.json_representation_store())
    delete_place_order_fixture(create_order_val.id)


@allure.feature("store_test")
def test_find_order_by_id_no_valid_id(store_api):
    store_api.find_order_by_id(create_order_no_valid.id)
    store_api.status_code_should_be(404)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)
    store_api.assert_objects_is_equal(response_find_no_valid, store_api.json_representation())


@allure.feature("store_test")
@pytest.mark.parametrize("create_order_val", [create_order_valid])
def test_delete_order_by_id_valid(store_api, create_place_order_fixture, create_order_val):
    create_place_order_fixture(create_order_val)
    store_api.delete_order_by_id(create_order_val.id)
    store_api.status_code_should_be(200)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)
    store_api.assert_objects_is_equal(response_delete_valid, store_api.json_representation())


@allure.feature("store_test")
def test_delete_order_by_id_no_exist_id(store_api):
    store_api.delete_order_by_id(create_order_no_valid.id)
    store_api.status_code_should_be(404)
    store_api.assert_schema_is_valid(ERROR_DELETE_STORE_SCHEMA)
    store_api.assert_objects_is_equal(response_delete_no_valid, store_api.json_representation())
