import os
from datetime import datetime

def log_error(error):
    os.makedirs("logs",exist_ok=True)

    with open("logs/error.txt","a") as f:
        f.write(f"\n file_path: {os.path.abspath(__file__)}\n")
        f.write(f"error_file_path: {os.path.abspath("logs/error.logs")}\n")
        f.write(f"datetime: {datetime.now()}\n")
        

