import json
import os


FILE = "database/inventory.json"

def load_inventory():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as file:
            data = json.load(file)
        if isinstance(data, list):
            return data
    except:
        pass
    return []


def save_inventory(items):
    os.makedirs("database", exist_ok=True)
    with open(FILE, "w") as file:
        json.dump(items, file, indent=4)


def generate_item_id(items):
    max_id = 1000
    for item in items:
        try:
            value = int(item.get("item_id",item.get("id", 0)))
            if value > max_id:
                max_id = value
        except:
            pass
    return str(max_id + 1)


def add_item():
    items = load_inventory()

    print("\n================================")
    print("          ADD INVENTORY")
    print("================================")

    while True:
        name = input("Enter Item Name: ").strip()
        if name:
            break
        print("Item name cannot be empty!")

    while True:
        quantity = input("Enter Quantity: ").strip()
        try:
            quantity = float(quantity)
            if quantity >= 0:
                break
        except:
            pass
        print("Enter a valid quantity!")
    unit = input("Enter Unit: ").strip()

    item = {
        "item_id": generate_item_id(items),
        "item_name": name,
        "quantity": quantity,
        "unit": unit
    }
    items.append(item)
    save_inventory(items)
    print("Inventory item added successfully!")

def display_inventory():
    items = load_inventory()
    print("\n================================")
    print("           INVENTORY")
    print("================================")

    if not items:
        print("No inventory items!")
        return
    for item in items:
        print("Item ID :",item.get("item_id",item.get("id", "")))
        print("Name    :",item.get("item_name",item.get("name", "")))
        print("Quantity:",item.get("quantity",0))
        print("Unit    :",item.get("unit",""))
        print("--------------------------------")

def update_item():
    items = load_inventory()
    item_id = input("Enter Item ID: ").strip()

    for item in items:
        if (str(item.get("item_id",item.get("id", "")))== item_id):
            while True:
                quantity = input(
                    "Enter New Quantity: ").strip()
                try:
                    quantity = float(quantity)
                    if quantity >= 0:
                        break
                except:
                    pass
                print("Enter a valid quantity!")
            item["quantity"] = quantity
            save_inventory(items)
            print("Inventory updated successfully!")
            return
    print("Item not found!")


def delete_item():
    items = load_inventory()
    item_id = input(
        "Enter Item ID: ").isalnum
    new_items = []
    deleted = False
    for item in items:
        if (str(item.get("item_id",item.get("id", "")))== item_id):
            deleted = True
        else:
            new_items.append(item)
    if deleted:
        save_inventory(new_items)
        print("Item deleted successfully!")
    else:
        print("Item not found!")


def inventory_menu():
    while True:

        print("\n================================")
        print("            INVENTORY")
        print("================================")

        print("1. Add Item")
        print("2. Display Inventory")
        print("3. Update Quantity")
        print("4. Delete Item")
        print("5. Back")

        choice = input(
            "Enter choice: ")

        if choice == "1":
            add_item()
        elif choice == "2":
            display_inventory()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            break
        else:
            print("Invalid choice!")