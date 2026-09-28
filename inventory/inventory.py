import json
import os


FILE = "database/inventory.json"


def load_inventory():

    os.makedirs("database", exist_ok=True)

    if os.path.exists(FILE):

        with open(FILE, "r") as file:
            return json.load(file)

    return []


def save_inventory(inventory):

    with open(FILE, "w") as file:
        json.dump(inventory, file, indent=4)


def add_item():

    inventory = load_inventory()

    print("\n========== ADD INVENTORY ==========")

    item_id = input("Enter Item ID: ")
    while True:
            item_name = input("Enter Item Name: ")
            if not item_name.isalpha() or len(item_name) < 3:
                break                    
            print("Invalid name,please try again")

    quantity = int(input("Enter Quantity: "))
    unit = input("Enter Unit: ")

    if not quantity.isdigit():
        print("Quantity must be a number!")
        return

    for item in inventory:

        if item["id"] == item_id:
            print("Item ID already exists!")
            return

    new_item = {
        "id": item_id,
        "name": item_name,
        "quantity": int(quantity),
        "unit": unit
    }

    inventory.append(new_item)

    save_inventory(inventory)

    print("Inventory item added successfully!")


def display_inventory():

    inventory = load_inventory()

    print("\n========== INVENTORY ==========")

    if len(inventory) == 0:
        print("Inventory is empty!")
        return

    for item in inventory:

        print("------------------------------")
        print("ID       :", item["id"])
        print("Name     :", item["name"])
        print("Quantity :", item["quantity"])
        print("Unit     :", item["unit"])


def update_inventory():

    inventory = load_inventory()

    item_id = input("Enter Item ID: ")

    for item in inventory:

        if item["id"] == item_id:

            quantity = input("Enter New Quantity: ")

            if not quantity.isdigit():
                print("Quantity must be a number!")
                return

            item["quantity"] = int(quantity)

            save_inventory(inventory)

            print("Inventory updated successfully!")
            return

    print("Item not found!")


def delete_inventory():

    inventory = load_inventory()

    item_id = input("Enter Item ID to delete: ")

    for item in inventory:

        if item["id"] == item_id:

            inventory.remove(item)

            save_inventory(inventory)

            print("Inventory item deleted!")
            return

    print("Item not found!")


def inventory_management():

    while True:

        print("\n================================")
        print("          INVENTORY")
        print("================================")

        print("1. Add Item")
        print("2. Display Inventory")
        print("3. Update Inventory")
        print("4. Delete Item")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_item()

        elif choice == "2":
            display_inventory()

        elif choice == "3":
            update_inventory()

        elif choice == "4":
            delete_inventory()

        elif choice == "5":
            break

        else:
            print("Invalid choice!")