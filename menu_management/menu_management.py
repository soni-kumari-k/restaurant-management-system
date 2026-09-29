import json
import os


FILE = "database/food_menu.json"


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

    while True:

        food_id = input("Enter Food ID (4 digit): ")

        if food_id.isdigit() and len(food_id) == 4:
            break

        print("Food ID must contain exactly 4 digits!")

    for food in menu:

        if food["id"] == food_id:

            print("Food ID already exists!")
            return

    while True:

        name = input("Enter Food Name: ").strip()

        if name.isalpha() and len(name.replace(" ","")) >= 3:
            break

        print("Invalid food name! Please try again.")

    while True:

        price = input("Enter Price: ")

        if price.isdigit() and int(price) > 0:
            break

        print("Price must be a positive number!")

    while True:

        category = input("Enter Category: ").strip()

        if category:
            break

        print("Category cannot be empty!")

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

    print("\n========================================================")
    print("                     FOOD MENU")
    print("========================================================")

    if len(menu) == 0:

        print("No food available!")
        return

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


def update_food():

    menu = load_menu()

    while True:

        food_id = input("Enter Food ID to update: ")

        if food_id.isdigit() and len(food_id) == 4:
            break

        print("Food ID must contain exactly 4 digits!")

    for food in menu:

        if food["id"] == food_id:

            while True:

                name = input("Enter New Name: ").strip()

                if name.isalpha() and len(name.replace(" ","")) >= 3:
                    break

                print("Invalid food name!")

            while True:

                price = input("Enter New Price: ")

                if price.isdigit() and int(price) > 0:
                    break

                print("Price must be a positive number!")

            while True:

                category = input("Enter New Category: ").strip()

                if category:
                    break

                print("Category cannot be empty!")

            food["name"] = name
            food["price"] = int(price)
            food["category"] = category

            save_menu(menu)

            print("Food updated successfully!")
            return

    print("Food not found!")


def delete_food():

    menu = load_menu()

    while True:

        food_id = input("Enter Food ID to delete: ")

        if food_id.isdigit() and len(food_id) == 4:
            break

        print("Food ID must contain exactly 4 digits!")

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

            print("Invalid choice! Please try again.")