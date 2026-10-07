import json
import os
from datetime import datetime

TABLE_FILE = "database/tables.json"
BOOKING_FILE = "database/bookings.json"

def load_json(file):
    if not os.path.exists(file):
        return []
    try:
        with open(file, "r") as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
    except:
        pass
    return []

def save_json(file, data):
    os.makedirs("database", exist_ok=True)
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

def setup_tables():
    tables = load_json(TABLE_FILE)
    if not tables:
        tables = [
            {"table_id": "1001", "capacity": 8},
            {"table_id": "1002", "capacity": 8},
            {"table_id": "1003", "capacity": 4},
            {"table_id": "1004", "capacity": 4},
            {"table_id": "1005", "capacity": 2}
        ]
        save_json(TABLE_FILE, tables)
    return tables

def valid_datetime(date_text, time_text):
    try:
        value = datetime.strptime(
            date_text + " " + time_text,
            "%d-%m-%Y %I:%M %p"
        )
        if value < datetime.now():
            return None
        return value
    except:
        return None

def get_booked_seats(bookings, date_text, time_text):
    booked = {}
    for booking in bookings:
        if (booking.get("date") == date_text and
            booking.get("time") == time_text):
            for table in booking.get("tables", []):
                table_id = str(table.get("table_id", ""))
                seats = int(table.get("seats", 0))
                booked[table_id] = booked.get(table_id, 0) + seats
    return booked

def book_seats():
    tables = setup_tables()
    bookings = load_json(BOOKING_FILE)

    print("\n================================")
    print("          BOOK SEATS")
    print("================================")

    customer_name = input("Enter Customer Name: ").strip()

    if not customer_name:
        print("Customer name cannot be empty!")
        return

    while True:
        seats_text = input("Enter Required Seats: ").strip()
        if seats_text.isdigit() and int(seats_text) > 0:
            required_seats = int(seats_text)
            break
        print("Enter a valid number of seats!")

    date_text = input("Enter Date (DD-MM-YYYY): ").strip()
    time_text = input("Enter Time (HH:MM AM/PM): ").strip().upper()

    booking_time = valid_datetime(date_text, time_text)

    if booking_time is None:
        print("Invalid or past date/time!")
        return

    booked = get_booked_seats(bookings, date_text, time_text)
    available = []
    total_available = 0

    for table in tables:
        table_id = str(table.get("table_id", ""))
        capacity = int(table.get("capacity", 0))
        already_booked = booked.get(table_id, 0)
        free = capacity - already_booked

        if free > 0:
            available.append({
                "table_id": table_id,
                "free": free
            })
            total_available += free

    if total_available < required_seats:
        print("Not enough seats available!")
        return

    remaining = required_seats
    selected_tables = []

    for table in available:
        if remaining <= 0:
            break

        seats_from_table = min(remaining, table["free"])

        selected_tables.append({
            "table_id": table["table_id"],
            "seats": seats_from_table
        })

        remaining -= seats_from_table

    booking = {
        "booking_id": str(int(datetime.now().timestamp() * 1000)),
        "customer_name": customer_name,
        "required_seats": required_seats,
        "date": date_text,
        "time": time_text,
        "tables": selected_tables
    }

    bookings.append(booking)
    save_json(BOOKING_FILE, bookings)

    print("\nBooking successful!")
    print("Customer Name:", customer_name)
    print("Seats Booked :", required_seats)
    print("Date         :", date_text)
    print("Time         :", time_text)
    print("Allocated Tables:")

    for table in selected_tables:
        print(
            "Table",
            table["table_id"],
            "-",
            table["seats"],
            "seat(s)"
        )

def display_bookings():
    bookings = load_json(BOOKING_FILE)

    print("\n================================")
    print("          BOOKINGS")
    print("================================")

    if not bookings:
        print("No bookings available!")
        return

    for booking in bookings:
        print("Booking ID    :", booking.get("booking_id", ""))
        print("Customer Name :", booking.get("customer_name", ""))
        print("Seats         :", booking.get("required_seats", 0))
        print("Date          :", booking.get("date", ""))
        print("Time          :", booking.get("time", ""))

        for table in booking.get("tables", []):
            print(
                "Table",
                table.get("table_id", ""),
                "-",
                table.get("seats", 0),
                "seat(s)"
            )

        print("--------------------------------")

def available_seats():
    tables = setup_tables()
    bookings = load_json(BOOKING_FILE)

    date_text = input("Enter Date (DD-MM-YYYY): ").strip()
    time_text = input("Enter Time (HH:MM AM/PM): ").strip().upper()

    if valid_datetime(date_text, time_text) is None:
        print("Invalid or past date/time!")
        return

    booked = get_booked_seats(bookings, date_text, time_text)

    print("\nAvailable Seats")
    print("--------------------------------")

    total = 0

    for table in tables:
        table_id = str(table.get("table_id", ""))
        capacity = int(table.get("capacity", 0))

        free = capacity - booked.get(table_id, 0)

        print(
            "Table",
            table_id,
            ":",
            free,
            "seat(s) available"
        )

        total += free

    print("--------------------------------")
    print("Total Available Seats:", total)

def cancel_booking():
    bookings = load_json(BOOKING_FILE)

    if not bookings:
        print("No bookings available!")
        return

    customer_name = input("Enter Customer Name: ").strip()
    date_text = input("Enter Date (DD-MM-YYYY): ").strip()
    time_text = input("Enter Time (HH:MM AM/PM): ").strip().upper()

    matching = []

    for booking in bookings:
        if (
            booking.get("customer_name", "").lower() == customer_name.lower()
            and booking.get("date") == date_text
            and booking.get("time") == time_text
        ):
            matching.append(booking)

    if not matching:
        print("Booking not found!")
        return

    booking = matching[0]

    booked_seats = int(
        booking.get("required_seats", 0)
    )

    while True:
        seats_text = input("Enter Seats to Cancel: ").strip()

        if (
            seats_text.isdigit()
            and 0 < int(seats_text) <= booked_seats
        ):
            cancel_seats = int(seats_text)
            break

        print("Enter a valid number of seats!")

    if cancel_seats == booked_seats:
        bookings.remove(booking)
        save_json(BOOKING_FILE, bookings)
        print("Booking cancelled successfully!")
        return

    remaining = cancel_seats

    for table in booking.get("tables", []):
        if remaining <= 0:
            break

        table_seats = int(table.get("seats", 0))

        if table_seats <= remaining:
            remaining -= table_seats
            table["seats"] = 0
        else:
            table["seats"] = table_seats - remaining
            remaining = 0

    booking["tables"] = [
        t for t in booking.get("tables", [])
        if int(t.get("seats", 0)) > 0
    ]

    booking["required_seats"] = booked_seats - cancel_seats

    save_json(BOOKING_FILE, bookings)

    print(cancel_seats, "seats cancelled successfully!")

def table_booking():
    while True:
        print("\n================================")
        print("         TABLE BOOKING")
        print("================================")
        print("1. Book Seats")
        print("2. Display Bookings")
        print("3. Available Seats")
        print("4. Cancel Booking")
        print("5. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            book_seats()
        elif choice == "2":
            display_bookings()
        elif choice == "3":
            available_seats()
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")