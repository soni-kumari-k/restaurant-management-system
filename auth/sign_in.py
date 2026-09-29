import json
import os
import stdiomask

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

    if not os.path.exists(FILE):

        if role == "staff":
            print("No available staff!")
        else:
            print("User file not found!")

        return None

    with open(FILE, "r") as file:
        users = json.load(file)

    if role == "staff":

        staff_found = False

        for user in users:

            if user["role"] == "staff":

                staff_found = True
                break

        if not staff_found:

            print("No available staff!")
            return None


    while True:

        name = input("Enter User Name: ").strip()

        if name.isalpha() and len(name.replace(" ","")) >= 3:
            break

        print("Invalid name! Please try again.")

    while True:

        password = stdiomask.getpass(prompt="Enter Password: ",mask="*")

        if 8 <= len(password) <= 15:
            break

        print("invalid password or Password mustbe 8 to 15 characters!")

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