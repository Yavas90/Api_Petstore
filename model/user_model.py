from dataclasses import dataclass, asdict


@dataclass
class RequestCreateUserModel:
    id: int
    user_name: str
    first_name: str
    last_name: str
    email: str
    password: str
    phone: str
    user_status: str

    def generate_body(self):
        user_body = {
            "id": self.id,
            "username": self.user_name,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone,
            "userStatus": self.user_status
        }

        return user_body

    def to_dict(self):
        return asdict(self)

