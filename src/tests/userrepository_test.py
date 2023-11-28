import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()

        self.user_nalle = User('nalle', 'nalle111')
        self.user_puh = User('puh', 'puh2222')

    def test_create(self):
        user_repository.create(self.user_nalle)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_nalle.username)

    def test_find_all(self):
        user_repository.create(self.user_nalle)
        user_repository.create(self.user_puh)
        users = user_repository.find_all()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, self.user_nalle.username)
        self.assertEqual(users[1].username, self.user_puh.username)

    def test_find_by_username(self):
        user_repository.create(self.user_nalle)
        user = user_repository.find_by_username(self.user_nalle.username)

        self.assertEqual(user.username, self.user_nalle.username)
