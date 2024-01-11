import pytest
import allure
from data.user_data.user_data import (create_user_valid, response_user_valid, create_user_no_valid,
                                      response_user_no_valid,
                                      update_user_valid, response_update_valid, update_user_no_valid,
                                      response_update_no_valid,
                                      response_get_valid, response_get_no_valid, response_valid_del_user)
from fixture.user_fixture import create_user_valid_fixture, delete_user_valid_fixture
from schemas.user_schemas import CREATE_UPDATE_GET_USER_SCHEMA, DELETE_ERROR_USER_SCHEMA

pytest_plugins = ["fixture.user_fixture"]


@allure.feature("user_test")
@pytest.mark.parametrize("valid_create_user", [create_user_valid])
def test_create_user_valid(user_api, valid_create_user, delete_user_valid_fixture):
    user_api.create_user(valid_create_user)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)
    user_api.assert_objects_is_equal(response_user_valid, user_api.json_representation())
    delete_user_valid_fixture(valid_create_user.user_name)


@allure.feature("user_test")
@pytest.mark.parametrize("no_valid_create_user", [create_user_no_valid])
def test_create_user_no_valid(user_api, no_valid_create_user):
    user_api.create_user(no_valid_create_user)
    user_api.status_code_should_be(500)
    user_api.assert_schema_is_valid(DELETE_ERROR_USER_SCHEMA)
    user_api.assert_objects_is_equal(response_user_no_valid, user_api.json_representation())


@allure.feature("user_test")
@pytest.mark.parametrize("valid_create_user", [create_user_valid])
def test_update_user_valid(user_api, create_user_valid_fixture, valid_create_user, delete_user_valid_fixture):
    create_user_valid_fixture(valid_create_user)
    user_api.update_user(user_name=valid_create_user.user_name, json_body=update_user_valid)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)
    user_api.assert_objects_is_equal(response_update_valid, user_api.json_representation())
    delete_user_valid_fixture(valid_create_user.user_name)


@allure.feature("user_test")
def test_update_user_no_valid(user_api):
    user_api.update_user(user_name=update_user_no_valid.user_name, json_body=update_user_no_valid)
    user_api.status_code_should_be(500)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)
    user_api.assert_objects_is_equal(response_update_no_valid, user_api.json_representation())


@allure.feature("user_test")
@pytest.mark.parametrize("valid_create_user", [create_user_valid])
def test_get_user_by_name_valid(user_api, valid_create_user, create_user_valid_fixture,
                                delete_user_valid_fixture):
    create_user_valid_fixture(valid_create_user)
    user_api.get_user(valid_create_user.user_name)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)
    user_api.assert_objects_is_equal(response_get_valid, user_api.json_representation_user())
    delete_user_valid_fixture(valid_create_user.user_name)


@allure.feature("user_test")
def test_get_user_by_name_no_valid(user_api):
    user_api.get_user(create_user_no_valid.id)
    user_api.status_code_should_be(404)
    user_api.assert_schema_is_valid(CREATE_UPDATE_GET_USER_SCHEMA)
    user_api.assert_objects_is_equal(response_get_no_valid, user_api.json_representation())


@allure.feature("user_test")
@pytest.mark.parametrize("valid_create_user", [create_user_valid])
def test_delete_user_by_name_valid(user_api, create_user_valid_fixture, valid_create_user):
    create_user_valid_fixture(valid_create_user)
    user_api.delete_user(valid_create_user.user_name)
    user_api.status_code_should_be(200)
    user_api.assert_schema_is_valid(DELETE_ERROR_USER_SCHEMA)
    user_api.assert_objects_is_equal(response_valid_del_user, user_api.json_representation())


@allure.feature("user_test")
def test_delete_user_by_name_no_valid(user_api):
    user_api.delete_user(create_user_no_valid.user_name)
    user_api.status_code_should_be(404)
