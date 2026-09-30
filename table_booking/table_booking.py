import json
import os
import uuid
from datetime import datetime


FILE = "database/tables.json"


def load_tables():

    os.makedirs("database", exist_ok=True)

    if not os.path.exists(FILE):

        return []

    try:

        with open(FILE, "r") as file:
            return json.load(file)

    except:

        return []


def save_tables(tables):

    os.makedirs("database", exist_ok=True)

    with open(FILE, "w") as file:
        json.dump(tables, file, indent=4)


def book_table():

    tables = load_tables()

    print("\n========== BOOK TABLE ==========")

    table_id = str(uuid.uuid4().int)[:4]

    while True:

        customer_name = input("Enter Customer Name: ").strip()

        if customer_name.replace(" ","").isalpha() and len(customer_name.replace(" ","")) >= 3:

            break

        print("Invalid name! Please try again.")

    while True:

        date = input("Enter Date (DD-MM-YYYY): ").strip()

        try:

            datetime.strptime(date, "%d-%m-%Y")
            break

        except ValueError:

            print("Invalid date, try again")

    while True:

        time = input("Enter Time (HH:MM): ").strip()

        try:

            datetime.strptime(time, "%H:%M")
            break

        except ValueError:

            print("Invalid time, try again")

    booking = {
        "table_id": table_id,
        "customer_name": customer_name,
        "date": date,
        "time": time,
        "status": "Booked"
    }

    tables.append(booking)

    save_tables(tables)

    print("\nTable booked successfully!")
    print("Table ID:", table_id)


def display_tables():

    tables = load_tables()

    print("\n========== TABLE BOOKINGS ==========")

    if len(tables) == 0:

        print("No table bookings!")
        return

    for table in tables:

        print("------------------------------")
        print("Table ID      :", table["table_id"])
        print("Customer Name :", table["customer_name"])
        print("Date          :", table["date"])
        print("Time          :", table["time"])
        print("Status        :", table["status"])


def update_table():

    tables = load_tables()

    if len(tables) == 0:

        print("No table bookings!")
        return

    table_id = input("Enter Table ID to update: ").strip()

    for table in tables:

        if table["table_id"] == table_id:

            while True:

                customer_name = input("Enter New Customer Name: ").strip()

                if customer_name.isalpha() and len(customer_name.replace(" ","")) >= 3:

                    break

                print("Invalid name! Please try again.")

            while True:

                date = input("Enter New Date (DD-MM-YYYY): ").strip()

                try:

                    datetime.strptime(date, "%d-%m-%Y")
                    break

                except ValueError:

                    print("Invalid date, try again")

            while True:

                time = input("Enter New Time (HH:MM): ").strip()

                try:

                    datetime.strptime(time, "%H:%M")
                    break

                except ValueError:

                    print("Invalid time, try again")

            table["customer_name"] = customer_name
            table["date"] = date
            table["time"] = time
            table["status"] = "Booked"

            save_tables(tables)

            print("Table booking updated successfully!")
            return

    print("Table ID not found!")


def cancel_table():

    tables = load_tables()

    if len(tables) == 0:

        print("No table bookings!")
        return

    table_id = input("Enter Table ID to cancel: ").strip()

    for table in tables:

        if table["table_id"] == table_id:
            tables.remove(table)
            save_tables(tables)

            print("Table booking cancelled successfully!")
            return

    print("Table ID not found!")


def table_booking():

    while True:

        print("\n================================")
        print("         TABLE BOOKING")
        print("================================")

        print("1. Book Table")
        print("2. Display Tables")
        print("3. Update Booking")
        print("4. Cancel Booking")
        print("5. Back")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            book_table()

        elif choice == "2":

            display_tables()

        elif choice == "3":

            update_table()

        elif choice == "4":

            cancel_table()

        elif choice == "5":

            break

        else:

            print("Invalid choice! Please try again.")