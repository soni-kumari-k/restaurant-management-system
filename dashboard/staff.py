from table_booking.table_booking import table_booking
from order.order_management import order_management
from billing.billing import billing_menu


def staff_menu(user):

    while True:

        print("\n================================")
        print("          STAFF DASHBOARD")
        print("================================")

        print("1. Table Booking")
        print("2. Order Management")
        print("3. Billing")
        print("4. Logout")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            table_booking()

        elif choice == "2":
            order_management()

        elif choice == "3":
            billing_menu()

        elif choice == "4":
            print("Logged out!")
            break

        else:
            print("Invalid choice!")