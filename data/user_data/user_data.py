from model.user_model import RequestCreateUserModel
from model.general_model import ResponseModel

"""Валидные данные для создания пользователя"""
create_user_valid = RequestCreateUserModel(id=258, user_name="TestUser", first_name="Test",
                                           last_name="User", email="TestEmail", password="TestPass", phone="TestPhone",
                                           user_status=333)

"""Проверка ответа, при создании валидного пользователя"""
response_user_valid = ResponseModel(code=200, type="unknown", message=str(create_user_valid.id))

"""Не валидные данные для создания пользователя"""
create_user_no_valid = RequestCreateUserModel(id=True, user_name=True, first_name=True, last_name=True, email=True,
                                              password=True, phone=True, user_status=True)

"""Проверка ответа, при создании не валидного пользователя"""
response_user_no_valid = ResponseModel(500, "unknown", "something bad happened")

"""Валидные данные для обновления пользователя"""
update_user_valid = RequestCreateUserModel(id=10, user_name="UpdateUser", first_name="Update",
                                           last_name="User", email="UpdateEmail", password="UpdatePass",
                                           phone="UpdatePhone", user_status=5)

"""Проверка ответа, при обновлении пользователя с валидными данными"""
response_update_valid = ResponseModel(code=200, type="unknown", message=str(update_user_valid.id))

"""Не валидные данные для обновления пользователя"""
update_user_no_valid = RequestCreateUserModel(id="№", user_name=True, first_name=True, last_name=True, email=True,
                                              password=True, phone=True, user_status=True)

"""Проверка ответа, при обновлении пользователя с не валидными данными"""
response_update_no_valid = ResponseModel(500, "unknown", "something bad happened")


"""Данные для проверки поиска валидного пользователя"""
response_get_valid = RequestCreateUserModel(id=create_user_valid.id, user_name=create_user_valid.user_name,
                                            first_name=create_user_valid.first_name, last_name=create_user_valid.last_name,
                                            email=create_user_valid.email, password=create_user_valid.password,
                                            phone=create_user_valid.phone,
                                            user_status=create_user_valid.user_status)

"""Проверка ответа, при поиске не валидного пользователя"""
response_get_no_valid = ResponseModel(1, "error", "User not found")


"""Проверка ответа, при удаления валидного пользователя"""
response_valid_del_user = ResponseModel(200, "unknown", create_user_valid.user_name)
