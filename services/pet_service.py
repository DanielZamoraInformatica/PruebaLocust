import requests

class PetService:
    BASE_URL = "https://petstore.swagger.io/v2"

    def add_pet(self, pet_data):
        url = f"{self.BASE_URL}/pet"
        response = requests.post(url, json=pet_data, headers={"Content-Type": "application/json"})
        return response