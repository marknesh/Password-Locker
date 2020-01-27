import string
import pyperclip
import random


class Password:

    password_list = []

    def __init__(self, password):
        self.password = password

    def save_password(self):
        """
                                function to add the inputted password in the password list
                                """
        Password.password_list.append(self)

    def delete_password(self):
        Password.password_list.remove(self)




    @classmethod
    def display_password(cls):
        """
                                apply method that is used by the whole class
                                """
        return cls.password_list

    @classmethod
    def find_password(cls,number):
        """
                                find a particular password in the password_list
                                    """
        for password in cls.password_list:
            if password.password == number:
                return password
    @classmethod
    def copy_password(cls,number):
        """
                                    function that copies password to clipboard
                                    """
        found_password = Password.find_password(number)
        pyperclip.copy(found_password.password)














