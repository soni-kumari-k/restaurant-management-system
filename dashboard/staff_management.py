import json
import os

from auth.sign_up import signup
from auth.sign_in import signin
from dashboard.staff import staff_menu


FILE = "database/users.json"


def display_staff():

    if not os.path.exists(FILE):

        print("No staff available!")
        return

    with open(FILE, "r") as file:
        users = json.load(file)

    found = False

    print("\n================================")
    print("          STAFF LIST")
    print("================================")

    for user in users:

        if user["role"] == "staff":

            found = True

            print("------------------------------")
            print("User ID :", user["user_id"])
            print("Name    :", user["name"])
            print("Email   :", user["email"])

    if not found:

        print("No staff available!")


def remove_staff():

    if not os.path.exists(FILE):

        print("No staff available!")
        return

    with open(FILE, "r") as file:
        users = json.load(file)

    staff_id = input("Enter Staff User ID: ").strip()

    for user in users:

        if user["user_id"] == staff_id and user["role"] == "staff":

            users.remove(user)

            with open(FILE, "w") as file:
                json.dump(users, file, indent=4)

            print("Staff removed successfully!")
            return

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

        choice = input("Enter your choice: ")

        if choice == "1":

            signup("staff")

        elif choice == "2":

            display_staff()

        elif choice == "3":

            remove_staff()

        elif choice == "4":

            break

        else:

            print("Invalid choice! Please try again.")