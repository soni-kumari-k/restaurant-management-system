import json
import os

from auth.sign_up import admin_signup
from auth.sign_in import signin
from dashboard.admin import admin_menu
from dashboard.staff import staff_menu

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


def main_menu():
    while True:
        users = load_users()
        admin_exists = False
        for user in users:
            if user.get("role") == "admin":
                admin_exists = True
                break

        print("\n================================")
        print("       RESTAURANT MANAGEMENT")
        print("================================")

        if not admin_exists:

            print("1. Admin Sign Up")
            print("2. Exit")
        else:
            print("1. Admin Sign In")
            print("2. Staff Sign In")
            print("3. Exit")

        choice = input("Enter choice: ").strip()

        if not admin_exists:
            if choice == "1":
                admin_signup()
            elif choice == "2":
                print("Thank you!")
                break
            else:
                print("Invalid choice!")
        else:
            if choice == "1":
                user = signin("admin")
                if user:
                    admin_menu(user)
            elif choice == "2":
                user = signin("staff")
                if user:
                    staff_menu(user)
            elif choice == "3":
                print("Thank you!")
                break
            else:
                print("Invalid choice!")