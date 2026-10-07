import json
import os
import uuid
from order.order_management import load_orders

FILE = "database/bills.json"
TAX_RATE = 0.05

def load_bills():
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


def save_bills(bills):

    os.makedirs("database", exist_ok=True)

    with open(FILE, "w") as file:
        json.dump(bills, file, indent=4)


def generate_bill_id(bills):

    while True:
        bill_id = str(str(uuid.uuid4().int)[:10])
        found = False
        for bill in bills:
            if str(bill.get("bill_id","")) == bill_id:
                found = True
                break
        if not found:
            return bill_id
        

def find_order(orders,customer_name):
    for order in orders:
        if (str(order.get("customer_name",""))==customer_name):
            return order
    return None


def generate_bill():
    orders = load_orders()
    bills = load_bills()
    if not orders:
        print("No orders available!")
        return

    while True:
        customer_name = input("Enter User Name: ").strip()
        if customer_name.replace(" ","").isalpha() and len(customer_name.replace(" ","")) >= 3:
            break
        print("Invalid name! Please try again.")


    order = find_order(orders,customer_name)
    if order is None:
        print("Order not found!")
        return
    
    items = order.get("items",[])
    if not items:
        print("No items in this order!")
        return

    for bill in bills:
        if (str(bill.get("customer_name",""))==customer_name.lower()):
            print("Bill already generated ,for this customer!")
            return
    amount = 0
    for item in items:
        try:
            amount += float(item.get("total",0))
        except:
            pass
    tax = amount * TAX_RATE
    grand_total = amount + tax
    print("\n==============================================")
    print("                  BILL")
    print("==============================================")
    print("Customer Name:",customer_name)
    print("Order ID     :",order.get("order_id",""))
    print("----------------------------------------------")
    for item in items:
        print(item.get("food_name",""),"|",item.get(    "size",    ""),"| Qty:",
              item.get(    "quantity",    0),"|",item.get(    "total",    0))
    print("----------------------------------------------")
    print("Amount       :",amount)
    print("Tax (5%)     :",tax)
    print("Grand Total  :",grand_total)
    print("----------------------------------------------")

    while True:
        payment_method = input("Enter Payment Method (Cash/UPI): ").strip().lower()
        if payment_method == "cash":
            payment_method = "Cash"
            break
        elif payment_method == "upi":
            payment_method = "UPI"
            break
        else:
            print("Please enter only Cash or UPI!")

    bill = {"bill_id": generate_bill_id(bills),
        "order_id": order.get("order_id",""),
        "customer_name": customer_name,
        "items": items,
        "amount": amount,
        "tax": tax,
        "grand_total": grand_total,
        "payment_method": payment_method
    }
    bills.append(bill)
    save_bills(bills)
    print("Bill generated successfully!")
    print("Bill ID:",bill["bill_id"])

def display_bills():
    bills = load_bills()
    print("\n================================")
    print("             BILLS")
    print("================================")
    if not bills:
        print("No bills available!")
        return
    for bill in bills:
        print("Bill ID        :",bill.get(    "bill_id",    ""))
        print("Customer Name  :",bill.get(    "customer_name",    ""))
        print("Amount         :",bill.get(    "amount",    0))
        print("Tax (5%)       :",bill.get(    "tax",    0))
        print("Grand Total    :",bill.get(    "grand_total",    0))
        print("Payment Method :",bill.get(    "payment_method",    ""))
        print("--------------------------------")

def billing_menu():
    while True:
        print("\n================================")
        print("             BILLING")
        print("================================")
        print("1. Generate Bill")
        print("2. Display Bills")
        print("3. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            generate_bill()
        elif choice == "2":
            display_bills()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")
            