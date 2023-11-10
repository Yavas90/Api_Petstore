from helper.parser import Parser


class JsonParser(Parser):

    def find_json_vertex(self, json_data: dict, keys: list = None):
        """Поиск элемента в json"""
        items = self._get_data(keys=keys, data=json_data)
        return items
