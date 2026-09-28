import json


def signin():

    while True:
        name = input("Enter User Name: ")

        if name.isalpha() and len(name) >= 3:
            break

        print("Invalid name, please try again")

    while True:
        password = input("Enter Password: ")

        if len(password) >= 3:
            break

        print("Password must contain at least 3 characters!")

    with open("database/users.json", "r") as file:
        users = json.load(file)

    for user in users:
        if user["name"] == name and user["password"] == password:
            print("------- Sign In Successful -------")
            return user

    print("Invalid Name or Password")
    return None
