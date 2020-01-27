from password import Password
from user import User
import random
import string


def create_password(password):
    new_password = Password(password)
    return new_password


def create_username(username):
    new_username = User(username)
    return new_username


def save_username(user):
    user.save_username()


def save_password(password):
    password.save_password()

def delete_password(password):
    password.delete_password()


def display_username():
    return User.display_username()

def display_password():
    return Password.display_password()

def getpass(num):
    generatepassword = ''

    for n in range(num):
        x = random.randint(0,  50)
        generatepassword += string.printable[x]
    return generatepassword





def main():



    global password
    while True:
        print("type s to signup, t to login ,r to show credentials , d to delete all passwords")

        form = input()
        if form == "s":
            print("enter username")
            username = input()

            with open("username.txt",  "w") as userData:
                data = userData.write(username)
                save_username(create_username(username))
                print("enter password or type generate to Generate a new password")

                password = input()
                save_password(create_password(password))
                with open("password.text", "w") as passwordData:
                    datapassword = passwordData.write(password)
                    print("type show to  display your credentials")

                    dataInput = input()
                    if dataInput == "show":
                        for user in display_username():
                            print(f"username: ", {user.username})

                            if password == "generate":
                                save_password(create_password(getpass(12)))
                                with open("password.text", "w") as passwordData:
                                    datapassword = passwordData.write(getpass(12))

                                    for password in display_password():
                                        print(f"password: ", {getpass(12)})
                                        print("your password length is " + str(len(getpass(12))))
                                        return




                        for password in display_password():
                            print(f"password: ", {password.password})
                            print("your password length is " + str(len(password.password)))

        elif form =="t":
            print("enter username")
            username = input()
            with open("username.txt", "r") as handleUsername:
                userTool = handleUsername.read()
            if username == userTool:
                print("enter password")
            else:
                print("No such username exists please signup")
                break

            password = input()
            with open("password.text", "r") as handlePassword:
                passwordtool = handlePassword.read()
            if password == passwordtool:
                print("logged in successfully")
                break
            else:
                print("WRONG PASSWORD")


        elif form == "r":

            if display_username():
                for user in display_username():
                    if dataInput == "show":
                        for user in display_username():
                            print(f"username: ", {user.username})
                            for password in display_password():
                                print(f"password: ", {password.password})
                                print("your password length is " + str(len(password.password)))

            else:
                print("SORRY YOU HAVE NO CREDENTIALS")

        elif form == "d":
            for password in display_password():
                if delete_password(password):
                        print("all passwords deleted successfully")
                else:
                     print("you have no  saved passwords")



        else:
            print("PLEASE TYPE s OR t")


if __name__ == '__main__':
    main()


