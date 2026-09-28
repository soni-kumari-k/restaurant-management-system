from auth.sign_up import signup
from auth.sign_in import signin
from dashboard.staff import staff_menu


def staff_management():

    while True:

        print("\n================================")
        print("        STAFF MANAGEMENT")
        print("================================")

        print("1. Staff Sign Up")
        print("2. Staff Sign In")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            signup("staff")

        elif choice == "2":

            user = signin("staff")

            if user:
                staff_menu()

        elif choice == "3":

            break

        else:

            print("Invalid choice! Please try again.")