from auth.sign_up import signup
from auth.sign_in import signin
from dashboard.admin import admin_menu
from dashboard.staff import staff_menu



def main_menu():

    while True:

        print("\n==============================")
        print("   RESTAURANT MANAGEMENT")
        print("==============================")

        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            signup()

        elif choice == "2":

            user = signin()

            if user:

                if user["role"] == "admin":
                    admin_menu()

                elif user["role"] == "staff":
                    staff_menu()

        elif choice == "3":
            print("Thank you!")
            break
            

        else:
            print("Invalid choice!")
            return