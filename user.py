class User:
    username_list = []

    def __init__(self, username):
        self.username = username

    def save_username(self):
        User.username_list.append(self)

    @classmethod
    def display_username(cls):
        return cls.username_list











