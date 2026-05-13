import unittest

from app import app


class TestRoutes(unittest.TestCase):

    def setUp(self):

        app.config["TESTING"] = True

        self.client = app.test_client()

    def test_home_route(self):

        response = self.client.get("/")

        self.assertEqual(
            response.status_code,
            200
        )

    def test_invalid_generate_request(self):

        response = self.client.post(
            "/generate",
            json={
                "job_title": ""
            }
        )

        self.assertEqual(
            response.status_code,
            400
        )


if __name__ == "__main__":
    unittest.main()