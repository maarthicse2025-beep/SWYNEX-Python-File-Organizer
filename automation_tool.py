import os
import shutil
from datetime import datetime

def file_processing():
    # Sample data file create pannurom
    if not os.path.exists("data"):
        os.makedirs("data")

    with open("data/input.txt", "w") as f:
        f.write("apple, 10\n")
        f.write("banana, 20\n")
        f.write("orange, 15\n")
    
    print("1. File Processing Done - input.txt created")

def data_transformation():
    # Data ah clean panni, total calculate pannurom
    total = 0
    items = []

    with open("data/input.txt", "r") as f:
        for line in f:
            name, qty = line.strip().split(",")
            name = name.strip().upper()
            qty = int(qty.strip())
            total += qty
            items.append((name, qty))

    print("2. Data Transformation Done - Data cleaned")

    return items, total

def backup_files():
    # Backup folder create panni file ah copy pannurom
    if not os.path.exists("backup"):
        os.makedirs("backup")

    backup_name = f"backup/backup_{datetime.now().strftime('%d-%m-%Y_%H-%M')}.txt"
    shutil.copy("data/input.txt", backup_name)
    print(f"3. Backup Done - Saved as {backup_name}")

def report_generation(items, total):
    # Report ah thana create pannurom
    with open("report.txt", "w") as f:
        f.write("AUTOMATION REPORT\n")
        f.write(f"Date: {datetime.now().strftime('%d-%m-%Y %H:%M')}\n")
        f.write("------------------------\n")
        for name, qty in items:
            f.write(f"{name} : {qty}\n")
        f.write("------------------------\n")
        f.write(f"Total Quantity: {total}\n")
        f.write("Status: Completed\n")

    print("4. Report Generation Done - report.txt created")

def main():
    print("\n--- Automation Tool ---")
    print("1. Run Automation")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        file_processing()
        items, total = data_transformation()
        backup_files()
        report_generation(items, total)
        print("\nAll Tasks Automated Successfully!")
    else:
        print("Bye!")

main()
