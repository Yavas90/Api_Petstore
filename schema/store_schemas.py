
STORE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "petId": {"type": "integer"},
        "quantity": {"type": "integer"},
        "shipDate": {"type": "string"},
        "status": {"type": "string"},
        "complete": {"type": "boolean"}
    }
}

ERROR_DELETE_STORE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "code": {"type": "integer"},
        "type": {"type": "string"},
        "message": {"type": "string"}
    }
}