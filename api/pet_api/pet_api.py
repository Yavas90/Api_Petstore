"""Класс для обращения к pet Api"""
from api.base_api import BaseApi

GET_POST_DELETE_PET_BY_ID_ENDPOINT = "/v2/pet/"
POST_ADD_PET_TO_STORE = "/v2/pet"


class PetApi(BaseApi):

    """Получение pet по id"""
    def get_pet(self, get_pet_id):
        return self.get(endpoint=GET_POST_DELETE_PET_BY_ID_ENDPOINT,
                        id=get_pet_id)

    """Создание нового pet"""
    def add_pet_to_store(self, json_body):
        return self.post(endpoint=POST_ADD_PET_TO_STORE,
                         headers=self.HEADERS,
                         json=json_body.generate_data())

    """Обновление Name и Status по id"""
    def update_pet_by_id(self, pet_id, json_body):
        return self.post(endpoint=f"{GET_POST_DELETE_PET_BY_ID_ENDPOINT}{pet_id}",
                         headers=self._HEADERS_UPDATE,
                         json=json_body.update_data())

    """Удаление pet по id"""
    def delete_pet(self, pet_id):
        return self.delete(endpoint=GET_POST_DELETE_PET_BY_ID_ENDPOINT,
                           id=pet_id)
