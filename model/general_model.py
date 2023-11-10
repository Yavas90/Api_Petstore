from dataclasses import dataclass


@dataclass
class ResponseModel:
    code: int
    type: str
    message: str

    def response_body(self):
        resp_body = {
            "code": self.code,
            "type": self.type,
            "message": self.message
        }

        return resp_body