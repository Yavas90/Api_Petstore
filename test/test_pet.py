import pytest
import allure
from data.pet_data.pet_data import (add_pet_valid, response_add_pet_valid, add_pet_no_valid, response_add_pet_no_valid,
                                    response_get_pet_no_valid, update_pet_valid, response_update_pet_valid,
                                    update_pet_no_valid)
from schemas.pet_schemas import GET_POST_SCHEMA, GET_UPD_DEL_ERROR_SCHEMA
from fixture.pet_fixture import delete_pet_valid_fixture, create_pet_valid_fixture

pytest_plugins = ["fixture.pet_fixture"]


@allure.feature("pet_test")
@pytest.mark.parametrize("add_pet_val", [add_pet_valid])
def test_add_pet_with_valid_params(pet_api, add_pet_val, delete_pet_valid_fixture):
    pet_api.add_pet_to_store(add_pet_val)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_POST_SCHEMA)
    pet_api.assert_objects_is_equal(response_add_pet_valid, pet_api.json_representation_pet())
    delete_pet_valid_fixture(add_pet_valid.id)


@allure.feature("pet_test")
@pytest.mark.parametrize("add_pet_no_val", [add_pet_no_valid])
def test_add_pet_with_no_valid_params(pet_api, add_pet_no_val):
    pet_api.add_pet_to_store(add_pet_no_val)
    pet_api.status_code_should_be(500)
    pet_api.assert_schema_is_valid(GET_UPD_DEL_ERROR_SCHEMA)
    pet_api.assert_objects_is_equal(response_add_pet_no_valid, pet_api.json_representation())


@allure.feature("pet_test")
@pytest.mark.parametrize("add_pet_val", [add_pet_valid])
def test_get_pet_with_valid_id(pet_api, create_pet_valid_fixture, add_pet_val,
                               delete_pet_valid_fixture):
    create_pet_valid_fixture(add_pet_val)
    pet_api.get_pet(add_pet_val.id)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_POST_SCHEMA)
    pet_api.assert_objects_is_equal(response_add_pet_valid, pet_api.json_representation_pet())
    delete_pet_valid_fixture(add_pet_val.id)


@allure.feature("pet_test")
def test_get_pet_with_no_valid_id(pet_api):
    pet_api.get_pet(add_pet_no_valid.id)
    pet_api.status_code_should_be(404)
    pet_api.assert_schema_is_valid(GET_UPD_DEL_ERROR_SCHEMA)
    pet_api.assert_objects_is_equal(response_get_pet_no_valid, pet_api.json_representation())


@allure.feature("pet_test")
@pytest.mark.parametrize("add_pet_val", [add_pet_valid])
@pytest.mark.parametrize("update_pet_val", [update_pet_valid])
def test_update_pet_with_valid_id_and_params(pet_api, update_pet_val, add_pet_val,
                                             create_pet_valid_fixture, delete_pet_valid_fixture):
    create_pet_valid_fixture(add_pet_val)
    pet_api.update_pet_by_id(pet_id=add_pet_val.id, json_body=update_pet_val)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_UPD_DEL_ERROR_SCHEMA)
    pet_api.assert_objects_is_equal(response_update_pet_valid, pet_api.json_representation())
    delete_pet_valid_fixture(add_pet_val.id)


@allure.feature("pet_test")
@pytest.mark.parametrize("add_pet_val", [add_pet_valid])
@pytest.mark.parametrize("update_pet_no_val", [update_pet_no_valid])
def test_update_pet_with_no_valid_id_and_params(pet_api, add_pet_val, update_pet_no_val):
    pet_api.update_pet_by_id(pet_id=add_pet_no_valid.id, json_body=update_pet_no_val)
    pet_api.status_code_should_be(404)
    pet_api.assert_schema_is_valid(GET_UPD_DEL_ERROR_SCHEMA)
    pet_api.assert_objects_is_equal(response_get_pet_no_valid, pet_api.json_representation())


@allure.feature("pet_test")
@pytest.mark.parametrize("add_pet_val", [add_pet_valid])
def test_delete_pet_with_valid_id(pet_api, create_pet_valid_fixture, add_pet_val):
    create_pet_valid_fixture(add_pet_val)
    pet_api.delete_pet(add_pet_val.id)
    pet_api.status_code_should_be(200)
    pet_api.assert_schema_is_valid(GET_UPD_DEL_ERROR_SCHEMA)
    pet_api.assert_objects_is_equal(response_update_pet_valid, pet_api.json_representation())


@allure.feature("pet_test")
def test_delete_pet_with_no_valid_id(pet_api):
    pet_api.delete_pet(add_pet_no_valid.id)
    pet_api.status_code_should_be(404)
    pet_api.assert_schema_is_valid(GET_UPD_DEL_ERROR_SCHEMA)
    pet_api.assert_objects_is_equal(response_get_pet_no_valid, pet_api.json_representation())
