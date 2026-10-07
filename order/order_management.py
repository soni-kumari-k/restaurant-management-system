import json
import os
import uuid
from datetime import datetime
from menu_management.menu_management import (load_food,display_menu)

FILE = "database/orders.json"

def load_orders():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as file:
            data = json.load(file)
            return data
    except:
        pass
    return []

def save_orders(orders):
    os.makedirs("database", exist_ok=True)
    with open(FILE, "w") as file:
        json.dump(orders, file, indent=4)

def generate_order_id(orders):
    while True:
        order_id = str(uuid.uuid4().int)[:10]
        found = False
        for order in orders:
            if str(order.get("order_id", "")) == order_id:
                found = True
                break
        if not found:
            return order_id

def get_food(food_id, food):
    for item in food:
        current_id = str(item.get("food_id",item.get("id", "")))
        if current_id == food_id:
            return item
    return None

def find_customer_order(orders,customer_name):
    for order in orders:
        if (str(order.get(    "customer_name",    ""))==customer_name.strip().lower()):
            return order
    return None

def create_order():
    orders = load_orders()
    food = load_food()
    if not food:
        print("No food available!")
        return
    display_menu()
    customer_name = input("\nEnter Customer Name: ")
    if not customer_name.isalpha() :
        print("Customer name cannot be empty!")
        return
    existing = find_customer_order(
        orders,
        customer_name
    )
    if existing is not None:
        print("Order already exists for this customer.")
        print("Use Add Order to add more items.")
        return
    order = {
        "order_id": generate_order_id(orders),
        "customer_name": customer_name,
        "items": [],
        "amount": 0,
        "created_at": datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )
    }
    while True:

        food_id = input("\nEnter Food ID: ").strip()
        item = get_food(food_id,food)
        if item is None:
            print("Food not found!")
            continue
        
        size = input(
            "Enter Half or Full: "
        ).strip().lower()

        if size not in ["half", "full"]:

            print("Enter only Half or Full!" )
            continue
        while True:
            quantity = input("Enter Quantity: ").strip()
            if ( quantity.isdigit() and int(quantity) > 0):
                quantity = int(quantity)
                break
            print( "Enter a valid quantity!")
        if size == "half":price = float(item.get("half_price",0))
        else:
            price = float(item.get( "full_price", 0 ) )
        total = price * quantity
        order["items"].append({
            "food_id": str(item.get("food_id",item.get("id", ""))),
            "food_name": item.get("food_name",item.get("name", "")),
            "size": size,
            "quantity": quantity,
            "price": price,
            "total": total
        })

        order["amount"] += total
        more = input(
            "Add another item? (yes/no): "
        ).strip().lower()
        if more != "yes":
            break
    save_orders(
        orders + [order]
    )
    print("\nOrder created successfully!")
    print("Order ID:",order["order_id"]
    )


def add_order():
    orders = load_orders()
    food = load_food()

    if not food:
        print("No food available!")
        return

    if not orders:
        print("No order available! Create an order first.")
        return

    display_menu()

    customer_name = input("\nEnter Customer Name: ").strip()
    order = find_customer_order(orders, customer_name)

    if order is None:
        print("Customer order not found!")
        return

    if not isinstance(order.get("items"), list):
        order["items"] = []

    if not isinstance(order.get("amount"), (int, float)):
        order["amount"] = 0

    while True:
        food_id = input("\nEnter Food ID: ").strip()
        item = get_food(food_id, food)

        if item is None:
            print("Food not found!")
            continue

        size = input("Enter Half or Full: ").strip().lower()

        if size not in ["half", "full"]:
            print("Enter only Half or Full!")
            continue

        while True:
            quantity = input("Enter Quantity: ").strip()

            if quantity.isdigit() and int(quantity) > 0:
                quantity = int(quantity)
                break

            print("Enter a valid quantity!")

        if size == "half":
            price = float(item.get("half_price", 0))
        else:
            price = float(item.get("full_price", 0))

        total = price * quantity

        order["items"].append({
            "food_id": str(item.get("food_id", item.get("id", ""))),
            "food_name": item.get("food_name", item.get("name", "")),
            "size": size,
            "quantity": quantity,
            "price": price,
            "total": total
        })

        order["amount"] += total

        more = input("Add another item? (yes/no): ").strip().lower()

        if more != "yes":
            break

    save_orders(orders)
    print("Order updated successfully!")

def display_orders():
    orders = load_orders()

    print("\n================================")
    print("          ALL ORDERS")
    print("================================")

    if not orders:
        print("No orders available!")
        return

    for order in orders:
        print( "Order ID     :",order.get("order_id",""))
        print( "Customer Name:",order.get("customer_name","") )
        print( "Amount       :",order.get("amount",0) )

        items = order.get("items", [])
        for item in items:
            print("  ",item.get("food_name",""),"|",item.get("size",""),"|" 
            " Qty:",item.get("quantity",0),"| Total:",item.get("total",0))
        print("--------------------------------")


def delete_order():
    orders = load_orders()
    if not orders:
        print("No orders available!")
        return
    customer_name = input("Enter Customer Name: ").strip()
    new_orders = []
    deleted = False
    for order in orders:
        if (str(order.get("customer_name","")).strip().lower()==customer_name.lower()):
            deleted = True
        else:
            new_orders.append(order)
    if deleted:
        save_orders(new_orders)
        print("Order deleted successfully!")
    else:
        print("Order not found!")

def order_management():
    while True:

        print("\n================================")
        print("        ORDER MANAGEMENT")
        print("================================")

        print("1. Create Order")
        print("2. Add Order")
        print("3. Display Order")
        print("4. Delete Order")
        print("5. Back")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            create_order()
        elif choice == "2":
            add_order()
        elif choice == "3":
            display_orders()
        elif choice == "4":
            delete_order()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")