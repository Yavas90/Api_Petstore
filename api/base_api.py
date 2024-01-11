import requests
import allure
from jsonschema import validate
from helper.logger import log
from typing import Union
from helper.json_parser import JsonParser
from model.user_model import RequestCreateUserModel
from model.store_model import ResponseStoreModel
from model.pet_model import RequestPetModel
from model.general_model import ResponseModel

"""Класс с Базовыми методами и asserts"""

BASE_URL = "https://petstore.swagger.io"


class BaseApi:
    HEADERS = {
        "accept": "application/json",
        "Content-Type": "application/json"
    }

    _HEADERS_UPDATE = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    def __init__(self):
        self.json_parser = JsonParser()
        self.response = None

    def get(self, endpoint: str, id: int):
        url = BASE_URL
        with allure.step(f"GET запрос на url: {url}{endpoint}"):
            self.response = requests.get(url=f"{url}{endpoint}{id}",
                                         headers=self.HEADERS)
        log(response=self.response)
        return self

    def post(self, endpoint: str, headers: dict = None, json: dict = None):
        url = BASE_URL
        with allure.step(f"POST запрос на url: {url}{endpoint}\n тело запроса: \n {json}"):
            self.response = requests.post(url=f"{url}{endpoint}",
                                          headers=headers,
                                          json=json)
        log(self.response, request_body=json)
        return self

    def put(self, endpoint: str, headers: dict = None, json: dict = None):
        url = BASE_URL
        with allure.step(f"PUT запрос на url: {url}{endpoint}\n тело запроса: \n {json}"):
            self.response = requests.put(url=f"{url}{endpoint}",
                                         headers=headers,
                                         json=json)
        log(self.response, request_body=json)
        return self

    def delete(self, endpoint: str, id: str):
        url = BASE_URL
        self.response = requests.delete(url=f"{url}{endpoint}{id}",
                                        headers=self.HEADERS)
        log(response=self.response)
        return self

    def status_code_should_be(self, expected_status_code: int):
        actual_status_code = self.response.status_code
        assert actual_status_code == expected_status_code, (f"Actual status code {actual_status_code}, "
                                                            f"Expected status code {expected_status_code}")
        return self

    def assert_schema_is_valid(self, expected_schema):
        validate(self.response.json(), expected_schema)
        return self

    def assert_equal_value_in_response_parameter(self, keys: list, value: Union[bool, str], decode: bool = False):
        """Параметр decode = False(по умолчанию) - xml response"""
        payload = self.get_payload(keys, decode)
        """проверяем на равенство ожидаемого значения и фактического"""
        assert value == payload, f"\nОжидаемый результат: {value} " \
                                 f"\nФактический результат: {payload}"
        return self

    def get_payload(self, keys: list, decode: bool = False):
        """Получаем payload переходя по ключам,
        и возвращаем полученный payload.
        decode=False -> xml: decode=True -> json"""
        if decode:
            """парсим в json"""
            response = self.response.json()
            payload = self.json_parser.find_json_vertex(response, keys)
        else:
            pass
        return payload

    def assert_objects_is_equal(self, exp_obj, act_obj):
        assert exp_obj == act_obj, f"\nОжидаемый результат: {exp_obj} " \
                                   f"\nФактический результат: {act_obj}"
        return self

    def json_representation(self) -> Union[ResponseModel, list]:
        payload = self.get_payload([], decode=True)
        return ResponseModel(code=payload['code'],
                             type=payload['type'],
                             message=payload['message'])

    def json_representation_user(self) -> Union[RequestCreateUserModel, list]:
        payload = self.get_payload([], decode=True)
        return RequestCreateUserModel(id=payload['id'],
                                      user_name=payload['username'],
                                      first_name=payload['firstName'],
                                      last_name=payload['lastName'],
                                      email=payload['email'],
                                      password=payload['password'],
                                      phone=payload['phone'],
                                      user_status=payload['userStatus'])

    def json_representation_store(self) -> Union[ResponseStoreModel, list]:
        payload = self.get_payload([], decode=True)
        return ResponseStoreModel(id=payload['id'],
                                  pet_id=payload['petId'],
                                  quantity=payload['quantity'],
                                  ship_date=payload['shipDate'],
                                  status=payload['status'],
                                  complete=payload['complete'])

    def json_representation_pet(self):
        payload = self.get_payload([], decode=True)
        return RequestPetModel(id=payload['id'],
                               category_id=payload['category']['id'],
                               category_name=payload['category']['name'],
                               name=payload['name'],
                               photo_urls=payload['photoUrls'],
                               tags_id=payload['tags'][0]['id'],
                               tags_name=payload['tags'][0]['name'],
                               status=payload['status'])
