import unittest
from app import create_app
from app.services import facade


class test_user_endpoint(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "John",
            "last_name": "Doe",
            "email": "janedoe@gmail.com",
            "is_admin": False
        })
        self.assertEqual(response.status_code, 201)

    def test_create_user_invalid_first_name(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "doe",
            "email": "john.doe@exemple.com",
            "is_admin": False
        })
        self.assertEqual(response.status_code, 400)

    def test_create_user_invalid_last_name(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "john",
            "last_name": "",
            "email": "john.doe@exemple.com",
            "is_admin": False
        })
        self.assertEqual(response.status_code, 400)

    def test_create_user_invalid_email(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "john",
            "last_name": "doe",
            "email": "invalid-email",
            "is_admin": False
        })
        self.assertEqual(response.status_code, 400)

    def test_create_user_invalid_is_admin(self):
        response = self.client.post('/api/v1/users/', json={
            "first_name": "john",
            "last_name": "doe",
            "email": "johndoe@gmail.com",
            "is_admin": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_get_user(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_id(self):
        user = facade.create_user({
            "first_name": "Jane",
            "last_name": "Moe",
            "email": "janemoe@gmail.com",
            "is_admin": False
        })
        address = f"/api/v1/users/{user.id}"
        response = self.client.get(address)
        self.assertEqual(response.status_code, 200)

    def test_get_user_by_id_invalid_id(self):
        response = self.client.get('/api/v1/users/azerty123456')
        self.assertEqual(response.status_code, 404)

    def test_update_user(self):
        user = facade.create_user({
            "first_name": "Jane",
            "last_name": "Loe",
            "email": "janeloe@gmail.com",
            "is_admin": False
        })
        address = f"/api/v1/users/{user.id}"
        response = self.client.put(address, json={
            "first_name": "John",
            "last_name": "Loe",
            "email": "johnloe@gmail.com",
            "is_admin": False
        })
        self.assertEqual(response.status_code, 200)

    def test_update_user_invalid_id(self):
        response = self.client.put('/api/v1/users/azerty123456', json={
            "first_name": "John",
            "last_name": "Loe",
            "email": "johnloe@gmail.com",
            "is_admin": False
        })
        self.assertEqual(response.status_code, 404)

    def test_update_user_invalid_first_name(self):
        user = facade.create_user({
            "first_name": "Jane",
            "last_name": "Loe",
            "email": "janeloe@gmail.com",
            "is_admin": False
        })
        address = f"/api/v1/users/{user.id}"
        response = self.client.put(address, json={
            "first_name": "",
            "last_name": "Loe",
            "email": "johnloe@gmail.com",
            "is_admin": False
        })
        self.assertEqual(response.status_code, 400)

    def test_update_user_invalid_last_name(self):
        user = facade.create_user({
            "first_name": "Jane",
            "last_name": "Loe",
            "email": "janeloe@gmail.com",
            "is_admin": False
        })
        address = f"/api/v1/users/{user.id}"
        response = self.client.put(address, json={
            "first_name": "John",
            "last_name": "",
            "email": "johnloe@gmail.com",
            "is_admin": False
        })
        self.assertEqual(response.status_code, 400)

    def test_update_user_invalid_email(self):
        user = facade.create_user({
            "first_name": "Jane",
            "last_name": "Loe",
            "email": "janeloe@gmail.com",
            "is_admin": False
        })
        address = f"/api/v1/users/{user.id}"
        response = self.client.put(address, json={
            "first_name": "John",
            "last_name": "Loe",
            "email": "not_an_email",
            "is_admin": False
        })
        self.assertEqual(response.status_code, 400)

    def test_update_user_invalid_is_admin(self):
        user = facade.create_user({
            "first_name": "Jane",
            "last_name": "Loe",
            "email": "janeloe@gmail.com",
            "is_admin": False
        })
        address = f"/api/v1/users/{user.id}"
        response = self.client.put(address, json={
            "first_name": "John",
            "last_name": "Loe",
            "email": "johnloe@gmail.com",
            "is_admin": "not_a_bool"
        })
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
