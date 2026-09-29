from table_booking.table_booking import table_booking
from order.order_management import order_management
from billing.billing import billing


def staff_menu():

    while True:

        print("\n================================")
        print("          STAFF DASHBOARD")
        print("================================")

        print("1. Table Booking")
        print("2. Order Management")
        print("3. Billing")
        print("4. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":

            table_booking()

        elif choice == "2":

            order_management()

        elif choice == "3":

            billing()

        elif choice == "4":

            print("Staff Logout successful!")
            break

        else:

            print("Invalid choice! Please try again.")