import unittest
from ..app import App


class RouteTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app_instance = App()
        cls.client = cls.app_instance.app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.app_instance.close()

    def test_user_login(self):
        response = self.client.post(
            "/user/login", json={"username": "testuser", "password": "password123"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("Login successful", response.get_data(as_text=True))

    def test_user_register(self):
        response = self.client.post(
            "/user/register",
            json={
                "username": "newuser",
                "password": "newpassword",
                "email": "newuser@example.com",
            },
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("User registered successfully", response.get_data(as_text=True))

    def test_get_current_user(self):
        response = self.client.get("/user")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Current user details", response.get_data(as_text=True))

    def test_get_notification_history(self):
        user_id = 1
        stream_id = 1
        response = self.client.get(f"/notification/user/{user_id}/stream/{stream_id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn("List of notifications", response.get_data(as_text=True))

    def test_process_video(self):
        response = self.client.post("/image_processing/process")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Video processed successfully", response.get_data(as_text=True))

    def test_integrate_stream(self):
        response = self.client.post(
            "/image_processing/stream_integration",
            json={"stream_url": "http://example.com/stream"},
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn("Stream integrated successfully", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()
