import unittest
from services.book_service import BookService


class TestBookService(unittest.TestCase):
    def setUp(self):
        self.bookservice = BookService()
        self.bookservice.create_user(username="jep", password="jup")

    def test_create_user_adds_user(self):
        response = self.bookservice._users.get("jep")

        self.assertEqual(response, "jup")

    def test_login_returns_true_with_correct_credentials(self):
        response = self.bookservice.login(username="jep", password="jup")

        self.assertTrue(response)

    def test_login_returns_false_with_incorrect_credentials(self):
        response = self.bookservice.login(username="ei", password="ei")

        self.assertFalse(response)
