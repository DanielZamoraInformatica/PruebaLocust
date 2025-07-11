import random

def generate_pet_payload():
    pet_id = random.randint(10000, 99999)
    return {
        "id": pet_id,
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "name": "Rex",
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [
            {
                "id": 0,
                "name": "bulldog"
            }
        ],
        "status": "available"
    }