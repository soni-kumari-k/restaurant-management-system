import json
import os
import uuid
import stdiomask

FILE = "database/users.json"

def signup(role):

    if role == "admin":

        print("\n================================")
        print("           ADMIN SIGN UP")
        print("================================")

    else:

        print("\n================================")
        print("           STAFF SIGN UP")
        print("================================")


    user_id = str(uuid.uuid4().int)[:10]   
    while True:
        name = input("Enter Name: ").strip()
        if name.replace(" ","").isalpha() and len(name.replace(" ","")) >= 3:
            break
        print("Invalid name! Please try again.")

    while True:
        email = input("Enter Email: ").strip()
        if "@" in email and "." in email:
            break
        print("Invalid email! Please try again.")

    while True:
        password = stdiomask.getpass(prompt="Enter Password: ",mask="*")
        if 8 <= len(password) <= 15:
            break
        print("Password must be 8 to 15 characters!")

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
        
    if role == "admin":
        for user in users:
            if user["role"] == "admin":
                print("Admin already exists!")
                return


    new_user = {
        "user_id": user_id,
        "name": name,
        "email": email,
        "password": password,
        "role": role
    }

    users.append(new_user)

    with open(FILE, "w") as file:
        json.dump(users, file, indent=4)

    print("\nRegistration Successful!")
    print("Your User ID:", user_id)