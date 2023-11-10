from api.pet_api.pet_api import PetApi
import pytest

"""Конектор к PetApi """


@pytest.fixture(scope="function")
def pet_api() -> PetApi:
    return PetApi()


@pytest.fixture(scope="function")
def create_pet_valid_fixture(pet_api):
    def _create_pet_valid_fixture(*args):
        pet_api.add_pet_to_store(*args)
    return _create_pet_valid_fixture


@pytest.fixture(scope="function")
def delete_pet_valid_fixture(pet_api):
    def _delete_pet_valid_fixture(*args):
        pet_api.delete_pet(*args)
    return _delete_pet_valid_fixture
