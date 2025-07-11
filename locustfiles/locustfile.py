from locust import HttpUser, task, between
from utils.pet_payloads import generate_pet_payload

class PetStoreUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def create_pet(self):
        pet = generate_pet_payload()
        headers = {"Content-Type": "application/json"}
        self.client.post("/v2/pet", json=pet, headers=headers)