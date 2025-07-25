pet_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "category": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"}
            },
            "required": ["id", "name"]
        },
        "name": {"type": "string"},
        "photoUrls": {
            "type": "array",
            "items": {"type": "string"}
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                },
                "required": ["id", "name"]
            }
        },
        "status": {
            "type": "string",
            "enum": ["available", "pending", "sold"]
        }
    },
    "required": ["id", "category", "name", "photoUrls", "tags", "status"]
}
