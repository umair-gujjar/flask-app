import unittest
from app import app, db
from app.models import User


class UserModelCase(unittest.TestCase):
    def test_user_creation(self):
        u = User(username='karthikrk1')
        self.assertTrue(u.username=='karthikrk1')
        self.assertFalse(u.username=='samy1')