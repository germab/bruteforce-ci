from unittest import TestCase
from BruteForce.password import Password


class TestPassword(TestCase):
    def test_check(self):
        pwd = Password("abc")
        self.assertEqual(True, pwd.check("abc"))

    def test_check2(self):
        pwd = Password("bca")
        self.assertEqual(False, pwd.check("abc"))
