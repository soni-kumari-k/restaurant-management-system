import json
import os
import uuid
import stdiomask

FILE = "database/users.json"

def load_users():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as file:
            data = json.load(file)
            return data
    except: 
        return []

def save_users(users):
    os.makedirs("database", exist_ok=True)
    with open(FILE, "w") as file:
        json.dump(users, file, indent=4)

def password_input():
    if stdiomask:
        return stdiomask.getpass(
            prompt="Enter Password: ",mask="*")
    from getpass import getpass
    return getpass("Enter Password: ")

def generate_id(users):
    while True:
        new_id = str(uuid.uuid4().int)[:10]
        found = False
        for user in users:
            if str(user.get("user_id", "")) == new_id:
                found = True
                break
        if not found:
            return new_id

def add_staff():
    users = load_users()

    print("\n================================")
    print("           ADD STAFF")
    print("================================")

    while True:
        name = input("Enter User Name: ").strip()
        if name.replace(" ","").isalpha() and len(name.replace(" ","")) >= 3:
            break
        print("Invalid name! Please try again.")
        
    while True:

        email = input("Enter Email: ").strip()
        if "@" not in email or "." not in email:
            print("Enter a valid email!")
            continue

        duplicate = False
        for user in users:
            if user.get("email", "").lower() == email.lower():
                duplicate = True
                break

        if duplicate:
            print("Email already exists!")
        else:
            break
    while True:
        password = password_input()
        if 8 <= len(password) <= 15:
            break
        print("Password must be 8 to 15 characters!")

    staff = {
        "user_id": generate_id(users),
        "name": name,
        "email": email,
        "password": password,
        "role": "staff"
    }

    users.append(staff)
    save_users(users)
    print("Staff added successfully!")
    print("Staff User ID:", staff["user_id"])


def display_staff():
    users = load_users()

    print("\n================================")
    print("          STAFF LIST")
    print("================================")

    found = False
    for user in users:
        if user.get("role") == "staff":
            found = True

            print("User ID :", user.get("user_id", ""))
            print("Name    :", user.get("name", ""))
            print("Email   :", user.get("email", ""))
            print("--------------------------------")

    if not found:
        print("No staff available!")


def remove_staff():
    users = load_users()

    print("\n================================")
    print("          REMOVE STAFF")
    print("================================")

    staff_found = False
    for user in users:
        if user.get("role") == "staff":
            staff_found = True
            break
    if not staff_found:
        print("No staff available!")
        return

    user_id = input("Enter Staff User ID: ").strip()
    new_users = []
    removed = False

    for user in users:
        if (user.get("role") == "staff" and str(user.get("user_id", "")) == user_id):
            removed = True
        else:
            new_users.append(user)
    if removed:
        save_users(new_users)
        print("Staff removed successfully!")
    else:
        print("Staff not found!")


def staff_management():
    while True:

        print("\n================================")
        print("        STAFF MANAGEMENT")
        print("================================")

        print("1. Add Staff")
        print("2. Display Staff")
        print("3. Remove Staff")
        print("4. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_staff()
        elif choice == "2":
            display_staff()
        elif choice == "3":
            remove_staff()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")