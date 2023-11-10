"""Данные для создания pet"""
from model.pet_model import RequestUpdatePetModel, RequestPetModel
from model.general_model import ResponseModel

"""Валидные данные для добавления животного"""
add_pet_valid = RequestPetModel(id=123, category_id=12, category_name="CategoryName1",
                                name="Name1", photo_urls="Test string1", tags_id=321,
                                tags_name="TagsName1", status="available")

"""Проверка ответа, при добавлении животного с валидными данными"""
response_add_pet_valid = RequestPetModel(id=add_pet_valid.id, category_id=add_pet_valid.category_id,
                                         category_name=add_pet_valid.category_name,
                                         name=add_pet_valid.name, photo_urls=[add_pet_valid.photo_urls],
                                         tags_id=add_pet_valid.tags_id,
                                         tags_name=add_pet_valid.tags_name, status=add_pet_valid.status)

"""Не валидные данные для добавления животного"""
add_pet_no_valid = RequestPetModel(id="Test", category_id="TestCatID", category_name=1,
                                    name=2, photo_urls=3, tags_id="TestTagsID",
                                    tags_name=4, status=False)

"""Проверка ответа, при добавлении животного с не валидными данными"""
response_add_pet_no_valid = ResponseModel(code=500, type="unknown", message="something bad happened")

"""Проверка ответа, при поиске животного с не валидными данными"""
response_get_pet_no_valid = ResponseModel(code=404, type="unknown",
                                               message=f"java.lang.NumberFormatException: For input string: \"{add_pet_no_valid.id}\"")

"""Валидные данные для изменения животного"""
update_pet_valid = RequestUpdatePetModel(name="UpdateName", status="UpdateStatus")

"""Проверка ответа, при изменении животного с валидными данными"""
response_update_pet_valid = ResponseModel(code=200, type="unknown", message=str(add_pet_valid.id))

"""Не валидные данные для изменения животного"""
update_pet_no_valid = RequestUpdatePetModel(name=123, status=321)