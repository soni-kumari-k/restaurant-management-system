import json
import os


FILE = "database/users.json"


def signin(role):

    if role == "admin":

        print("\n================================")
        print("           ADMIN SIGN IN")
        print("================================")

    else:

        print("\n================================")
        print("           STAFF SIGN IN")
        print("================================")

    while True:

        name = input("Enter User Name: ").strip()

        if name.isalpha() and len(name) >= 3:
            break

        print("Invalid name! Please try again.")

    while True:

        password = input("Enter Password: ")

        if 8 <= len(password) <= 15:
            break

        print("Password must be 8 to 15 characters!")

    if not os.path.exists(FILE):

        print("User file not found!")
        return None

    with open(FILE, "r") as file:
        users = json.load(file)

    for user in users:

        if (
            user["name"] == name
            and user["password"] == password
            and user["role"] == role
        ):

            print("\n------- Sign In Successful -------")

            return user

    print("\nInvalid Name or Password!")

    return None