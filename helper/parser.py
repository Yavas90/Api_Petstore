"""Класс с общими методами для парсеров данных"""
from typing import Union


class Parser:

    @staticmethod
    def _get_data(keys: Union[list, str], data: Union[dict, list]):
        """Получение полезной нагрузки по ключам,
        если нагрузки нет возвращаем пустой dict"""
        body = data
        for key in keys:
            try:
                body = body[key]
                if body is None:
                    return {}
            except KeyError:
                raise KeyError(f'Отсутствуют данные для ключа {key}')
        return body