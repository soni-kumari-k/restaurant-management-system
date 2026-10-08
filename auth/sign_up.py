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
        if isinstance(data, list):
            return data
    except:
        pass
    return []

def save_users(users):
    os.makedirs("database", exist_ok=True)
    with open(FILE, "w") as file:
        json.dump(users, file, indent=4)

def generate_user_id(users):
    while True:
        user_id = str(uuid.uuid4().int)[:10]
        found = False
        for user in users:
            if str(user.get("user_id", "")) == user_id:
                found = True
                break
        if not found:
            return user_id

def get_password():

    if stdiomask:
        return 
    stdiomask.getpass(prompt="Enter Password: ",mask="*")
    from getpass import getpass
    return getpass("Enter Password: ")

def signup(role):
    users = load_users()
    print("\n================================")
    print("       " + role.upper() + " SIGN UP")
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
        password = get_password()
        if 8 <= len(password) <= 15:
            break
        print("Password must be 8 to 15 characters!")

    user = {
        "user_id": generate_user_id(users),
        "name": name,
        "email": email,
        "password": password,
        "role": role
    }
    users.append(user)
    save_users(users)
    print("\nRegistration successful!")
    print("Your User ID:", user["user_id"])

def admin_signup():
    users = load_users()
    for user in users:
        if user.get("role") == "admin":
            print("Admin already exists!")
            return
    signup("admin")