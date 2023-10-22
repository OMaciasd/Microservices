import unittest
import sys
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(base_dir, '..', 'app')
if app_path not in sys.path:
    sys.path.append(app_path)

from app import create_app

app = create_app('testing')

class TestDevOpsApp(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.testing = True
        self.client = self.app.test_client()
        response_jwt = self.client.get('/generate-jwt')

        print(response_jwt.status_code)

        json_data = response_jwt.get_json()
        if json_data:
            self.valid_jwt = json_data.get("token", None)
        else:
            self.valid_jwt = None

    def post_to_devops(self, headers, data=None):
        return self.client.post('/devops', headers=headers, json=data)

    def test_generate_jwt(self):
        response = self.client.get('/generate-jwt')
        self.assertEqual(response.status_code, 200)

        print(response.data)

    # def test_devops_endpoint_post(self):
    #     headers = {
    #         'X-Parse-REST-API-Key': '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c',
    #         'X-JWT-KWY': self.valid_jwt,
    #         'Content-Type': 'application/json'
    #     }
    #     data = {
    #         'message': 'Test Message',
    #         'to': 'Test Receiver',
    #         'from': 'Test Sender',
    #         'timeToLifeSec': 30
    #     }
    #     response = self.post_to_devops(headers, data)  # Usar el método de apoyo

    #     # Check HTTP status code
    #     self.assertEqual(response.status_code, 200)

    #     # Check response content
    #     json_data = response.get_json()
    #     self.assertEqual(json_data["message"], "Hello Test Receiver your message will be send")

    # def test_devops_endpoint_get(self):
    #     response = self.client.get('/DevOps')
    #     self.assertEqual(response.data, b'ERROR')
    #     self.assertEqual(response.status_code, 405)

    # def test_invalid_api_key(self):
    #     headers = {
    #         'X-Parse-REST-API-Key': 'invalid_api_key',
    #         'X-JWT-KWY': self.valid_jwt,
    #         'Content-Type': 'application/json'
    #     }
    #     response = self.post_to_devops(headers)  # Usar el método de apoyo
    #     self.assertEqual(response.status_code, 401)

    # def test_invalid_jwt(self):
    #     headers = {
    #         'X-Parse-REST-API-Key': '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c',
    #         'X-JWT-KWY': 'invalid_jwt_token',
    #         'Content-Type': 'application/json'
    #     }
    #     response = self.post_to_devops(headers)
    #     self.assertEqual(response.status_code, 401)

    # def test_incomplete_payload(self):
    #     headers = {
    #         'X-Parse-REST-API-Key': '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c',
    #         'X-JWT-KWY': self.valid_jwt,
    #         'Content-Type': 'application/json'
    #     }
    #     data = {'message': 'Test Message'}  # Payload incompleto
    #     response = self.client.post('/DevOps', headers=headers, json=data)
    #     self.assertEqual(response.status_code, 400)

    # def test_devops_endpoint_put(self):
    #     headers = {
    #         'X-Parse-REST-API-Key': '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c',
    #         'X-JWT-KWY': self.valid_jwt
    #     }
    #     response = self.client.put('/DevOps', headers=headers)
    #     self.assertEqual(response.data.decode("utf-8"), "ERROR")
    #     self.assertEqual(response.status_code, 405)

if __name__ == "__main__":
    unittest.main()
