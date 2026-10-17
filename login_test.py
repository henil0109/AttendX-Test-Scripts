"""AttendX login automation test (SIMULATED).

This file does NOT connect to a real AttendX application. It uses a small
in-memory FakeLoginService to demonstrate how login test cases are written,
assert results, and version-controlled with Git.

Run:  python login_test.py -v
"""
import unittest


class FakeLoginService:
    """Simulated AttendX login backend with a fixed set of users."""

    def __init__(self):
        self._users = {
            "teacher01": "Pass@123",
            "student01": "Study@456",
        }

    def login(self, username, password):
        """Return a dict describing the login result."""
        if self._users.get(username) == password and password is not None:
            return {"success": True, "message": "Login successful", "user": username}
        return {"success": False, "message": "Invalid username or password", "user": None}


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.service = FakeLoginService()

    def test_valid_credentials_login_succeeds(self):
        result = self.service.login("teacher01", "Pass@123")
        self.assertTrue(result["success"])
        self.assertEqual(result["message"], "Login successful")
        self.assertEqual(result["user"], "teacher01")

    def test_wrong_password_is_rejected(self):
        result = self.service.login("teacher01", "wrong-password")
        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Invalid username or password")
        self.assertIsNone(result["user"])

    def test_unknown_user_is_rejected(self):
        result = self.service.login("ghost_user", "Pass@123")
        self.assertFalse(result["success"])
        self.assertIsNone(result["user"])


if __name__ == "__main__":
    unittest.main()
