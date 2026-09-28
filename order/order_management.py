import json
import os
import uuid


MENU_FILE = "database/food_menu.json"
ORDER_FILE = "database/orders.json"


def load_menu():

    if os.path.exists(MENU_FILE):

        with open(MENU_FILE, "r") as file:
            return json.load(file)

    return []


def load_orders():

    if os.path.exists(ORDER_FILE):

        with open(ORDER_FILE, "r") as file:
            return json.load(file)

    return []


def save_orders(orders):

    os.makedirs("database", exist_ok=True)

    with open(ORDER_FILE, "w") as file:
        json.dump(orders, file, indent=4)


def create_order():

    menu = load_menu()
    orders = load_orders()

    if len(menu) == 0:

        print("No food available in menu!")
        return

    print("\n========================================================")
    print("                     FOOD MENU")
    print("========================================================")

    print(
            "ID","      ",        
            "FOOD NAME","       ",     
            "PRICE","       ",     
            "CATEGORY","        "      
        )

    print("--------------------------------------------------------")

    for food in menu:

        print(
                    food["id"],"        " ,     
                    food["name"],"      ",       
                    food["price"],"        ",      
                    food["category"],"      "        
                )

    print("========================================================")

    order_id = str(uuid.uuid4().int)[:10]

    while True:

        customer_name = input("Enter Customer Name: ").strip()

        if customer_name.isalpha() and len(customer_name) >= 3:
            break

        print("Invalid name! Please try again.")

    while True:

        food_id = input("Enter Food ID: ")

        if food_id.isdigit() and len(food_id) == 4:
            break

        print("Food ID must contain exactly 4 digits!")

    while True:

        quantity = input("Enter Quantity: ")

        if quantity.isdigit() and int(quantity) > 0:
            break

        print("Quantity must be greater than 0!")

    quantity = int(quantity)

    for food in menu:

        if food["id"] == food_id:

            total = food["price"] * quantity

            new_order = {
                "order_id": order_id,
                "customer_name": customer_name,
                "food_id": food["id"],
                "food_name": food["name"],
                "quantity": quantity,
                "price": food["price"],
                "total": total
            }

            orders.append(new_order)

            save_orders(orders)

            print("Order created successfully!")
            print("Order ID:", order_id)
            print("Total Amount: Rs.", total)

            return

    print("Food not found!")


def display_orders():

    orders = load_orders()

    print("\n========== ORDERS ==========")

    if len(orders) == 0:

        print("No orders available!")
        return

    for order in orders:

        print("------------------------------")
        print("Order ID      :", order["order_id"])
        print("Customer      :", order["customer_name"])
        print("Food          :", order["food_name"])
        print("Quantity      :", order["quantity"])
        print("Price         :", order["price"])
        print("Total         :", order["total"])


def order_management():

    while True:

        print("\n================================")
        print("        ORDER MANAGEMENT")
        print("================================")

        print("1. Create Order")
        print("2. Display Orders")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "1":

            create_order()

        elif choice == "2":

            display_orders()

        elif choice == "3":

            break

        else:

            print("Invalid choice!")