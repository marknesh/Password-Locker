import string

import random


class Password:

    password_list = []

    def __init__(self, password):
        self.password = password

    def save_password(self):
        Password.password_list.append(self)



    @classmethod
    def display_password(cls):
        return cls.password_list





# def getpass(num):
#     password = ''
#
#     for n in range(num):
#         x = random.randint(0,  50)
#         password += string.printable[x]
#     return password
#
#
# print(len(getpass(12)))
#
#
# print(getpass(12))





