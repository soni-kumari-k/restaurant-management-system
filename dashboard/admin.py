from menu_management.menu_management import menu_management
from table_booking.table_booking import table_booking
from order.order_management import order_management
from billing.billing import billing_menu
from inventory.inventory import inventory_menu
from dashboard.staff_management import staff_management
from logs.logs import logs_menu

def admin_menu(user):
    while True:
        print("\n================================")
        print("          ADMIN DASHBOARD")
        print("================================")

        print("1. Menu Management")
        print("2. Table Booking")
        print("3. Order Management")
        print("4. Billing")
        print("5. Inventory")
        print("6. Staff Management")
        print("7. Logs")
        print("8. Logout")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            menu_management()
        elif choice == "2":
            table_booking()
        elif choice == "3":
            order_management()
        elif choice == "4":
            billing_menu()
        elif choice == "5":
            inventory_menu()
        elif choice == "6":
            staff_management()
        elif choice == "7":
            logs_menu()
        elif choice == "8":
            print("Logged out!")
            break
        else:
            print("Invalid choice!")