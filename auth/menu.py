import json
import os

from auth.sign_up import signup
from auth.sign_in import signin
from dashboard.admin import admin_menu
from dashboard.staff import staff_menu


FILE = "database/users.json"


def admin_exists():

    if not os.path.exists(FILE):
        return False

    with open(FILE, "r") as file:
        users = json.load(file)

    for user in users:

        if user["role"] == "admin":
            return True

    return False


def main_menu():

    while True:

        print("\n================================")
        print("      RESTAURANT MANAGEMENT")
        print("================================")

        if not admin_exists():

            print("1. Admin Sign Up")
            print("2. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":

                signup("admin")

                user = signin("admin")

                if user:
                    admin_menu()

            elif choice == "2":

                print("Thank you!")
                break

            else:

                print("Invalid choice! Please try again.")

        else:

            print("1. Admin Sign In")
            print("2. Staff Sign In")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":

                user = signin("admin")

                if user:
                    admin_menu()

            elif choice == "2":

                user = signin("staff")

                if user:
                    staff_menu()

            elif choice == "3":

                print("Thank you!")
                break

            else:

                print("Invalid choice! Please try again.")