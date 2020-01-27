import unittest
from user import User
from password import Password
import pyperclip


class TestPassword(unittest.TestCase):
    def setUp(self):
        self.new_username = User("mark")
        self.new_password = Password("99990")

    def test_init(self):
        self.assertEqual(self.new_username.username, "mark")
        self.assertEqual(self.new_password.password, "99990")


    def test_save_username(self):
        self.new_username.save_username()
        self.assertEqual(len(User.username_list), 1)

    def test_save_password(self):
        self.new_password.save_password()
        self.assertEqual(len(Password.password_list), 1)

    def tearDown(self):
        Password.password_list = []
        User.username_list = []

    def test_display_password(self):
        self.new_password.save_password()
        test_password = Password("44444")
        test_password.save_password()
        self.assertEqual(Password.display_password(), Password.password_list)

    def test_display_username(self):
        self.new_username.save_username()
        test_username = User("mark")
        test_username.save_username()

        self.assertEqual(User.display_username(), User.username_list)

    def test_copy_password(self):
        self.new_password.save_password()
        test_password = Password("9999")
        test_password.save_password()
    def test_delete_password(self):
        self.new_password.save_password()
        test_password = Password("dwdw")
        test_password.save_password()
        self.new_password.delete_password()
        self.assertEqual(len(Password.password_list), 1)

    def test_find_password(self):
        self.new_password.save_password()
        test_password = Password("090909")
        test_password.save_password()
        found_password = Password.find_password("090909")
        self.assertEqual(found_password.password, test_password.password)
        # self.assertEqual(self.new_password.password, pyperclip.paste())

    # @classmethod
    # def find_by_number(cls, number):
    #     for password in cls.password_list:
    #         if .phone_number == number:
    #             return contact







             











if __name__ == '__main__':
    unittest.main()
