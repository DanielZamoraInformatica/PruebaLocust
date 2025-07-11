import unittest
from services.pet_service import PetService
from utils.pet_payloads import generate_pet_payload

class TestAddPet(unittest.TestCase):

    def setUp(self):
        self.service = PetService()
        self.pet_data = generate_pet_payload()

    def test_add_pet_success(self):
        response = self.service.add_pet(self.pet_data)
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertEqual(response_data["name"], self.pet_data["name"])
        self.assertEqual(response_data["status"], self.pet_data["status"])
        self.assertIn("id", response_data)

if __name__ == "__main__":
    unittest.main()