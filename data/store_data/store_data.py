from model.store_model import RequestStoreModel, ResponseStoreModel
from model.general_model import ResponseModel
import datetime

"""Валидные данные для создания заказа на животное"""
create_order_valid = RequestStoreModel(id=3, pet_id=0, quantity=12,
                                     ship_date=datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"+0000",
                                     status="placed", complete=True)

"""Проверка ответа, при создании заказа на животное с валидными данными"""
response_create_order_valid = ResponseStoreModel(id=create_order_valid.id, pet_id=create_order_valid.pet_id,
                                               quantity=create_order_valid.quantity,
                                               ship_date=create_order_valid.ship_date, status=create_order_valid.status,
                                               complete=bool(create_order_valid.complete))

"""Не валидные данные для создания заказа на животное"""
create_order_no_valid = RequestStoreModel(id="abc", pet_id="zxc", quantity="rtyr", status=123, complete=4444, ship_date=False)

"""Проверка ответа, при создании заказа на животное с не валидными данными"""
response_create_order_no_valid = ResponseModel(code=500, type="unknown", message="something bad happened")

"""Проверка ответа, при поиске заказа на животное с валидными данными"""
response_find_valid = ResponseStoreModel(id=create_order_valid.id, pet_id=create_order_valid.pet_id,
                                               quantity=create_order_valid.quantity,
                                               ship_date=create_order_valid.ship_date, status=create_order_valid.status,
                                               complete=bool(create_order_valid.complete))

"""Проверка ответа, при поиске заказа на животное с не валидными данными"""
response_find_no_valid = ResponseModel(code=404, type="unknown",
                                            message=f"java.lang.NumberFormatException: For input string: \"{create_order_no_valid.id}\"")

"""Проверка ответа, при удалении заказа на животное с валидными данными"""
response_delete_valid = ResponseModel(code=200, type="unknown", message=str(create_order_valid.id))

"""Проверка ответа, при удалении заказа на животное с не валидными данными"""
response_delete_no_valid = ResponseModel(code=404, type="unknown", message=f"java.lang.NumberFormatException: For input string: \"{create_order_no_valid.id}\"")
