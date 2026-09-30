import json
import os
import uuid


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

    while True:

        item_id = str(uuid.uuid4().int)[:4]

        if item_id.isdigit() and len(item_id) == 4:
            break

        print("Item ID must contain exactly 4 digits!")

    for item in inventory:

        if item["id"] == item_id:

            print("Item ID already exists!")
            return

    while True:

        item_name = input("Enter Item Name: ").strip()

        if item_name.replace(" ","").isalpha() and len(item_name.replace(" ","")) >= 3:
            break

        print("Invalid item name! Please try again.")

    while True:

        quantity = input("Enter Quantity: ")

        if quantity.isdigit() and int(quantity) > 0:
            break

        print("Quantity must be greater than 0!")

    while True:

        unit = input("Enter Unit: ").strip()

        if unit:
            break

        print("Unit cannot be empty!")

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

    while True:

        item_id = input("Enter Item ID: ")

        if item_id.isdigit() and len(item_id) == 4:
            break

        print("Item ID must contain exactly 4 digits!")

    for item in inventory:

        if item["id"] == item_id:

            while True:

                quantity = input("Enter New Quantity: ")

                if quantity.isdigit() and int(quantity) > 0:
                    break

                print("Quantity must be greater than 0!")

            item["quantity"] = int(quantity)

            save_inventory(inventory)

            print("Inventory updated successfully!")
            return

    print("Item not found!")


def delete_inventory():

    inventory = load_inventory()

    while True:

        item_id = input("Enter Item ID to delete: ")

        if item_id.isdigit() and len(item_id) == 4:
            break

        print("Item ID must contain exactly 4 digits!")

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