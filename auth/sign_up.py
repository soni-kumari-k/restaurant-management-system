import json
import os


FILE = "database/users.json"


def signup():

    print("\n==============================")
    print("           SIGN UP")
    print("==============================")

    while True:

        name = input("Enter Name: ").strip()

        if name.isalpha() and len(name) >= 3:
            break

        print("Invalid name! Please try again.")


    while True:

        email = input("Enter Email: ").strip()

        if "@" in email and "." in email:
            break

        print("Invalid email! Please try again.")


    while True:

        password = input("Enter Password: ")

        if password.isalnum() and len(password) >= 3:
            break

        print("Password must be atleast 3 characters")

    os.makedirs("database", exist_ok=True)

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

    