import pytest
from api.user_api.user_api import UserApi


"""Конектор к UserApi """


@pytest.fixture(scope="function")
def user_api() -> UserApi:
    return UserApi()


@pytest.fixture(scope="function")
def create_user_valid_fixture(user_api):
    def _create_user_valid_fixture(*args):
        user_api.create_user(*args)

    return _create_user_valid_fixture


@pytest.fixture(scope="function")
def delete_user_valid_fixture(user_api):
    def _delete_user_valid_fixture(*args):
        user_api.delete_user(*args)

    return _delete_user_valid_fixture
