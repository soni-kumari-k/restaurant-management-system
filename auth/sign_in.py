import json
import os
import stdiomask

FILE = "database/users.json"

def load_users():

    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as file:
            data = json.load(file)

        if isinstance(data, list):
            return data
    except:
        pass
    return []

def get_password():

    if stdiomask:
        return stdiomask.getpass(prompt="Enter Password: ",mask="*")
    from getpass import getpass
    return getpass("Enter Password: ")


def signin(role):

    users = load_users()
    if role == "staff":
        staff_exists = False
        for user in users:
            if user.get("role") == "staff":
                staff_exists = True
                break
        if not staff_exists:
            print("\nNo available staff!")
            return None

    print("\n================================")
    print("       " + role.upper() + " SIGN IN")
    print("================================")

    email = input("Enter Email: ").strip()
    password = get_password()
    for user in users:
        if (
            user.get("email", "").lower() == email.lower()
            and user.get("password", "") == password
            and user.get("role") == role
        ):
            print("\nLogin successful!")
            return user
    print("Invalid email or password!")
    return None