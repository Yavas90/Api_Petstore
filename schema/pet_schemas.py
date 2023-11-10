"""Схемы ответа по pet"""

GET_POST_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "category": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"}}
        },
        "name": {"type": "string"},
        "photoUrls": {
            "type": "array",
            "properties": {
                "name": {"type": "string"}
            }
        },
        "tags": {
            "type": "array",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"}}
        },
        "status": {"type": "string"}
    }
}

GET_UPD_DEL_ERROR_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "code": {"type": "integer"},
        "type": {"type": "string"},
        "message": {"type": "string"}
    }
}

POST_EMPTY_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "photoUrls": {"type": "string"},
        "tags": {"type": "string"}
    }
}


RESP_EMPTY_SCHEMA = None
