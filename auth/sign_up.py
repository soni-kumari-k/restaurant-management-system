import json
import os


FILE = "data/users.json"


def signup():

    print("\n==============================")
    print("           SIGN UP")
    print("==============================")

    name = input("Enter Name: ").strip()

    if not name.isalpha() or len(name) < 3:
        print("Invalid name!")
        return

    email = input("Enter Email: ").strip()

    if "@" not in email or "." not in email:
        print("Invalid email!")
        return

    password = input("Enter Password: ")

    if len(password) < 3:
        print("Password must contain at least 3 characters!")
        return

    os.makedirs("data", exist_ok=True)

    if os.path.exists(FILE):

        with open(FILE, "r") as file:
            users = json.load(file)

    else:
        users = []

    for user in users:

        if user["email"] == email:
            print("Email already registered!")
            return

    admin_exists = False

    for user in users:

        if user["role"] == "admin":
            admin_exists = True
            break

    if admin_exists:

        role = "staff"

        print("Admin already exists.")
        print("New account will be created as Staff.")

    else:

        print("\nNo Admin account found.")
        print("You can create the Admin account.")

        role = input("Enter Role (admin/staff): ").lower()

        if role not in ["admin", "staff"]:
            print("Role must be admin or staff!")
            return

    new_user = {
        "name": name,
        "email": email,
        "password": password,
        "role": role
    }

    users.append(new_user)

    with open(FILE, "w") as file:
        json.dump(users, file, indent=4)

    print("\nRegistration successful!")
    print("Role:", role)
    print("You can now Sign In.")