import json
import os



ORDER_FILE = "database/orders.json"
BILL_FILE = "database/bills.json"


def load_orders():

    if os.path.exists(ORDER_FILE):

        with open(ORDER_FILE, "r") as file:
            return json.load(file)

    return []


def load_bills():

    if os.path.exists(BILL_FILE):

        with open(BILL_FILE, "r") as file:
            return json.load(file)

    return []


def save_bills(bills):

    os.makedirs("data", exist_ok=True)

    with open(BILL_FILE, "w") as file:
        json.dump(bills, file, indent=4)


def generate_bill():

    orders = load_orders()
    bills = load_bills()

    if len(orders) == 0:
        print("No orders available!")
        return

    order_id = input("Enter Order ID: ")

    for order in orders:

        if order["order_id"] == order_id:

            bill_id = input("Enter Bill ID: ")

            subtotal = order["total"]
            tax = subtotal * 0.05
            grand_total = subtotal + tax

            bill = {
                "bill_id": bill_id,
                "order_id": order_id,
                "customer_name": order["customer_name"],
                "subtotal": subtotal,
                "tax": tax,
                "grand_total": grand_total
            }

            bills.append(bill)

            save_bills(bills)

            print("\n========== BILL ==========")
            print("Bill ID       :", bill_id)
            print("Customer      :", order["customer_name"])
            print("Subtotal      : Rs.", subtotal)
            print("Tax 5%        : Rs.", tax)
            print("Grand Total   : Rs.", grand_total)
            print("==========================")

            return

    print("Order not found!")


def display_bills():

    bills = load_bills()

    print("\n========== ALL BILLS ==========")

    if len(bills) == 0:
        print("No bills available!")
        return

    for bill in bills:

        print("------------------------------")
        print("Bill ID       :", bill["bill_id"])
        print("Order ID      :", bill["order_id"])
        print("Customer      :", bill["customer_name"])
        print("Subtotal      :", bill["subtotal"])
        print("Tax           :", bill["tax"])
        print("Grand Total   :", bill["grand_total"])


def billing():

    while True:

        print("\n================================")
        print("            BILLING")
        print("================================")

        print("1. Generate Bill")
        print("2. Display Bills")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_bill()

        elif choice == "2":
            display_bills()

        elif choice == "3":
            break

        else:
            print("Invalid choice!")