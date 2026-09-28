import json
import os


FILE = "data/food_menu.json"


def load_menu():

    os.makedirs("database", exist_ok=True)

    if os.path.exists(FILE):

        with open(FILE, "r") as file:
            return json.load(file)

    return []


def save_menu(menu):

    with open(FILE, "w") as file:
        json.dump(menu, file, indent=4)


def add_food():

    menu = load_menu()

    print("\n========== ADD FOOD ==========")

    food_id = int(input("Enter Food ID(4 digit): "))
    while True:
        name = input("Enter Food Name: ")
        if not name.isalpha() or len(name) < 3:
            break            
        print("Invalid name,please try again")
    price = int(input("Enter Price: "))
    category = input("Enter Category: ")

    if food_id == "" or name == "" or price == "" or category == "":
        print("All fields are required!")
        return

    if not price.isdigit():
        print("Price must be a number!")
        return

    for food in menu:

        if food["id"] == food_id:
            print("Food ID already exists!")
            return

    new_food = {
        "id": food_id,
        "name": name,
        "price": int(price),
        "category": category
    }

    menu.append(new_food)

    save_menu(menu)

    print("Food added successfully!")


def display_food():

    menu = load_menu()

    print("\n========== FOOD MENU ==========")

    if len(menu) == 0:
        print("No food available!")
        return

    for food in menu:

        print("------------------------------")
        print("ID       :", food["id"])
        print("Name     :", food["name"])
        print("Price    :", food["price"])
        print("Category :", food["category"])


def update_food():

    menu = load_menu()

    food_id = int(input("Enter Food ID to update: "))

    for food in menu:

        if food["id"] == food_id:

            name = input("Enter New Name: ")
            price = input("Enter New Price: ")
            category = input("Enter New Category: ")

            if not price.isdigit():
                print("Price must be a number!")
                return

            food["name"] = name
            food["price"] = int(price)
            food["category"] = category

            save_menu(menu)

            print("Food updated successfully!")
            return

    print("Food not found!")


def delete_food():

    menu = load_menu()

    food_id = input("Enter Food ID to delete: ")

    for food in menu:

        if food["id"] == food_id:

            menu.remove(food)

            save_menu(menu)

            print("Food deleted successfully!")
            return

    print("Food not found!")


def menu_management():

    while True:

        print("\n================================")
        print("       MENU MANAGEMENT")
        print("================================")

        print("1. Add Food")
        print("2. Display Food")
        print("3. Update Food")
        print("4. Delete Food")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_food()

        elif choice == "2":
            display_food()

        elif choice == "3":
            update_food()

        elif choice == "4":
            delete_food()

        elif choice == "5":
            break

        else:
            print("Invalid choice!")