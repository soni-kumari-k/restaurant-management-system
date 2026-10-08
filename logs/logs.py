import os


INFO_FILE = "logs/info.txt"
ERROR_FILE = "logs/error.txt"


def setup_logs():

    os.makedirs("logs",exist_ok=True)
    if not os.path.exists(INFO_FILE):
        open(INFO_FILE,"w").close()
    if not os.path.exists(ERROR_FILE):
        open(ERROR_FILE,"w").close()

def read_log(file):
    setup_logs()
    try:
        with open(file,"r") as f:
            content = f.read()
        if content.strip() == "":
            print("No logs available!")
        else:
            print(content)
    except:
        print("Unable to read log!")

def logs_menu():
    setup_logs()
    while True:

        print("\n================================")
        print("              LOGS")
        print("================================")

        print("1. View Info Logs")
        print("2. View Error Logs")
        print("3. Back")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            print(
                "\n========== INFO LOGS =========="
            )
            read_log(INFO_FILE)
        elif choice == "2":
            print("\n========= ERROR LOGS ==========")
            read_log(ERROR_FILE)
        elif choice == "3":
            break
        else:
            print("Invalid choice!")