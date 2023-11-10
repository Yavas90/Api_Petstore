from dataclasses import dataclass, asdict


@dataclass
class RequestStoreModel:
    id: int
    pet_id: int
    quantity: int
    ship_date: str
    status: str
    complete: bool

    def generate_body(self):
        store_body = {
            "id": self.id,
            "petId": self.pet_id,
            "quantity": self.quantity,
            "shipDate": self.ship_date,
            "status": self.status,
            "complete": self.complete
        }

        return store_body

    def to_dict(self):
        return asdict(self)


@dataclass
class ResponseStoreModel:
    id: int
    pet_id: int
    quantity: int
    ship_date: str
    status: str
    complete: bool

    def generate_response(self):
        response_body = {
            "id": self.id,
            "petId": self.pet_id,
            "quantity": self.quantity,
            "shipDate": self.ship_date,
            "status": self.status,
            "complete": self.complete
        }

        return response_body
