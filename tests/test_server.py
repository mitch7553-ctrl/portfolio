import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import server


class PortfolioTests(unittest.TestCase):
    def setUp(self):
        self.client = server.app.test_client()

    def test_unknown_template_is_not_served(self):
        self.assertEqual(self.client.get("/server.py").status_code, 404)

    def test_invalid_contact_is_rejected(self):
        response = self.client.post("/submit_form", data={
            "email": "invalid", "subject": "Hello", "message": "Hi"
        })
        self.assertEqual(response.status_code, 400)

    def test_successful_contact_submission(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(server, "DATA_PATH", Path(tmp) / "contacts.csv"):
                response = self.client.post("/submit_form", data={
                    "email": "example@example.com", "subject": "Hello", "message": "Hi"
                })
                self.assertEqual(response.status_code, 303)
                self.assertTrue((Path(tmp) / "contacts.csv").exists())

    def test_get_submission_is_not_allowed(self):
        self.assertEqual(self.client.get("/submit_form").status_code, 405)


if __name__ == "__main__":
    unittest.main()
