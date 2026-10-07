import json
import os

FILE = "database/food_menu.json"

HEADINGS = [
    "NORTH INDIAN",
    "SOUTH INDIAN",
    "CHINESE",
    "ITALIAN",
    "DRINKS"
]

def load_food():
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

def save_food(food):
    os.makedirs("database", exist_ok=True)
    with open(FILE, "w") as file:
        json.dump(food, file, indent=4)

def generate_food_id(food):
    max_id = 1000
    for item in food:
        value = item.get("food_id",item.get("id", 0))
        try:
            value = int(value)
            if value > max_id:
                max_id = value
        except:
            pass
    return str(max_id + 1)

def display_menu():
    food = load_food()

    print("\n==============================================")
    print("                 FOOD MENU")
    print("==============================================")

    if not food:
        print("No food available!")
        return
    for heading in HEADINGS:
        heading_items = []
        for item in food:
            item_heading = str(
                item.get("heading", "")
            ).upper()
            if item_heading == heading:
                heading_items.append(item)
        if not heading_items:
            continue

        print("\n---------- " + heading + " ----------")
        print("ID     FOOD NAME              CATEGORY        HALF    FULL")
        print("----------------------------------------------------------")
        for item in heading_items:
            food_id = item.get("food_id",item.get("id", ""))
            name = item.get("food_name",item.get("name", ""))
            category = item.get("category", "")
            half = item.get("half_price", 0)
            full = item.get("full_price", 0)
            print(str(food_id),"  ",str(name),"  ",str(category),"  ",str(half),"  ",str(full))

def add_food():
    food = load_food()

    print("\n================================")
    print("             ADD FOOD")
    print("================================")

    while True:
        name = input("Enter Food Name: ").strip()
        if name == "":
            print("Food name cannot be empty!")
            continue
        duplicate = False
        for item in food:
            old_name = item.get("food_name",item.get("name", ""))
            if old_name.lower() == name.lower():
                duplicate = True
                break
        if duplicate:
            print("Food already exists!")
        else:
            break
    print("\nSelect Heading")
    for i in range(len(HEADINGS)):
        print(str(i + 1) + ".",HEADINGS[i])

    while True:
        choice = input("Enter heading choice: ").strip()
        if (choice.isdigit() and 1 <= int(choice) <= len(HEADINGS)):
            heading = HEADINGS[int(choice) - 1]
            break
        print("Invalid heading!")
    category = input("Enter Category: ").strip()

    while True:
        half = input("Enter Half Price: ").strip()
        try:
            half_price = float(half)
            if half_price >= 0:
                break
        except:
            pass
        print("Enter a valid price!")

    while True:
        full = input("Enter Full Price: ").strip()
        try:
            full_price = float(full)
            if full_price >= 0:
                break
        except:
            pass
        print("Enter a valid price!")
    item = {
        "food_id": generate_food_id(food),
        "food_name": name,
        "heading": heading,
        "category": category,
        "half_price": half_price,
        "full_price": full_price
    }
    food.append(item)
    save_food(food)
    print("Food added successfully!")
    print("Food ID:", item["food_id"])


def delete_food():
    food = load_food()

    print("\n================================")
    print("            DELETE FOOD")
    print("================================")

    food_id = input("Enter Food ID: ").strip()
    new_food = []
    deleted = False
    for item in food:
        item_id = str(item.get("food_id",item.get("id", "")))
        if item_id == food_id:
            deleted = True
        else:
            new_food.append(item)
    if deleted:
        save_food(new_food)
        print("Food deleted successfully!")
    else:
        print("Food not found!")


def menu_management():
    while True:

        print("\n================================")
        print("        MENU MANAGEMENT")
        print("================================")

        print("1. Add Food")
        print("2. Display Menu")
        print("3. Delete Food")
        print("4. Back")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_food()
        elif choice == "2":
            display_menu()
        elif choice == "3":
            delete_food()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")