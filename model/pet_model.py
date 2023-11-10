from dataclasses import dataclass, asdict

"""Метод и модель создания тестовых данных, для создания нового pet"""

"""Метод и модель создания тестовых данных, для обновления pet по id"""


@dataclass
class RequestPetModel:
    id: int
    category_id: int
    category_name: str
    name: str
    photo_urls: str
    tags_id: int
    tags_name: str
    status: str

    def generate_data(self):
        valid_create_data_test = {
            "id": self.id,
            "category": {
                "id": self.category_id,
                "name": self.category_name
            },
            "name": self.name,
            "photoUrls": [
                self.photo_urls
            ],
            "tags": [
                {
                    "id": self.tags_id,
                    "name": self.tags_name
                }
            ],
            "status": self.status
        }

        return valid_create_data_test

    def to_dict(self):
        return asdict(self)


@dataclass
class RequestUpdatePetModel:
    name: str
    status: str

    def update_data(self):
        return asdict(self)
